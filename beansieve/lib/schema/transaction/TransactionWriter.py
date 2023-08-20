import itertools

from beancount.core import data


class Transaction(object):

    def to_plain(self, connection):
        pass

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
