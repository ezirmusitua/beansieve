import itertools

from beancount.core import data


def empty_if_none(val):
    return "" if val is None else str(val)


def ensure_float_fixed(val: float):
    if val is None:
        return ""
    if isinstance(val, int):
        return str(val) + ".00"
    if isinstance(val, float) and val.is_integer():
        return str(val) + ".00"
    return str(val)


class Transaction(object):

    def cost_string(self, posting):
        cost_number = posting[6]
        cost_currency = empty_if_none(posting[7])
        cost_date = empty_if_none(posting[8])
        cost_label = empty_if_none(posting[9])
        out = ""
        if cost_number is not None:
            out = f"{cost_number} {cost_currency}"
        if cost_date != "":
            out = out + (", " if out else "") + cost_date
        if cost_label != "":
            out = out + (", " if out else "") + cost_label
        if out:
            return "{ " + out + " }"
        return ""

    def price_string(self, posting):
        price_number = posting[10]
        price_currency = posting[11]
        if price_number is not None:
            return f"@ {price_number} {price_currency}"
        return ""

    def to_plain(self, connection):
        sections = list()
        with connection:
            for row in connection.execute("SELECT * FROM transactions"):
                content = list()
                row = list(map(empty_if_none, row))
                date = row[1]
                flag = row[5]
                payee = row[6]
                narration = row[7]
                tags = " ".join(
                    list(map(lambda x: f"#{x}", filter(lambda x: x != "", row[8].split(",")))))
                links = " ".join(
                        list(map(lambda x: f"^{x}", filter(lambda x: x != "", row[9].split(",")))))
                content.append(
                    f"{date} {flag} \"{payee}\" \"{narration}\" {tags} {links}")
                postings = connection.execute(
                    f"SELECT * FROM postings WHERE id = {row[0]}")
                for posting in postings:
                    flag = empty_if_none(posting[2])
                    account = empty_if_none(posting[3])
                    number = ensure_float_fixed(posting[4])
                    currency = empty_if_none(posting[5])
                    posting_string = " ".join([
                        flag, account, number, currency, self.cost_string(
                            posting), self.price_string(posting)
                    ])
                    content.append(f"\t{posting_string}")
                sections.append("\n".join(content))
        return "\n\n".join(sections)

    def to_sql(self, connection, entries):
        self.create_table(connection)
        self.create_view(connection)
        postings_count = iter(itertools.count())
        with connection:
            for eid, entry in enumerate(entries):
                if not isinstance(entry, data.Transaction):
                    continue
                connection.execute("""
                  insert into entry values (?, ?, ?, ?, ?);
                """, (eid, entry.date, 'txn', entry.meta["filename"], entry.meta["lineno"]))

                connection.execute("""
                  insert into transactions_detail values (?, ?, ?, ?, ?, ?);
                """, (eid, entry.flag, entry.payee, entry.narration,
                      ','.join(entry.tags or ()), ','.join(entry.links or ())))

                self.insert_postings(
                    connection, eid, postings_count, entry.postings)

    def insert_postings(self, connection, eid: int, pid_getter, postings):
        for posting in postings:
            pid = next(pid_getter)
            units = posting.units
            cost = posting.cost
            price = posting.price
            connection.execute("""
              INSERT INTO postings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (pid, eid,
                  posting.flag,
                  posting.account,
                  units.number,
                  units.currency,
                  cost.number if cost else None,
                  cost.currency if cost else None,
                  cost.date if cost else None,
                  cost.label if cost else None,
                  price.number if price else None,
                  price.currency if price else None))

    def create_table(self, connection):
        """Create a table for transactions and fill in the data.

        Args:
          connection: A DBAPI-2.0 Connection object.
          entries: A list of directives.
        """
        with connection:
            connection.execute("""
              CREATE TABLE transactions_detail (
                id 			        INTEGER PRIMARY KEY,
                flag 		        CHARACTER(1),
                payee 		        VARCHAR,
                narration 		    VARCHAR,
                tags                VARCHAR, -- Comma-separated
                links               VARCHAR  -- Comma-separated
              );
            """)

            connection.execute("""
              CREATE TABLE postings (
                posting_id		    INTEGER PRIMARY KEY,
                id 			        INTEGER,
                flag                CHARACTER(1),
                account             VARCHAR,
                number              DECIMAL(16, 6),
                currency            CHARACTER(10),
                cost_number         DECIMAL(16, 6),
                cost_currency       CHARACTER(10),
                cost_date           DATE,
                cost_label          VARCHAR,
                price_number        DECIMAL(16, 6),
                price_currency      CHARACTER(10),
                FOREIGN KEY(id) REFERENCES entries(id)
              );
            """)

    def create_view(self, connection):
        connection.execute("""
          CREATE VIEW transactions AS
            SELECT * FROM entry 
            JOIN transactions_detail USING (id)
            ORDER BY date;
        """)
