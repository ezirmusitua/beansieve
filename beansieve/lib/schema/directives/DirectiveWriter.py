from typing import NamedTuple


class DirectiveWriter:
    """A base class for writers of directives.
    This is used to factor out code for all the simple directives types
    (all types except Transaction).
    """
    # The name of the type of the directive. Override this.
    type: NamedTuple

    # A string, the columns to create as a single multiline declaration.
    columns: str

    @property
    def field_count(self):
        return len(self.columns.splitlines())

    def __init__(self):
        self.name = self.type.__name__.lower()

    def to_plain(self, connection):
        lines = []
        with connection:
            for entry in connection.execute(f"SELECT * from {self.name}"):
                date = entry[1]
                directive = entry[2]
                fields = self.field_values(entry)
                line = " ".join([date, directive, *fields])
                lines.append(line)
        return "\n".join(lines)

    def to_sql(self, connection, entries):
        with connection:

            self.create_table(connection)
            self.create_view(connection)
            for eid, entry in enumerate(entries):
                if not isinstance(entry, self.type):
                    continue

                # Store common data.
                connection.execute("""
                 INSERT INTO entry VALUES (?, ?, ?, ?, ?);
               """, (eid, entry.date, self.name,
                     entry.meta["filename"], entry.meta["lineno"]))

                # Store detail data.
                detail_data = self.get_detail(entry)
                row_data = (eid,) + detail_data
                query = """
                 INSERT INTO {name}_detail VALUES ({placeholder});
               """.format(name=self.name,
                          placeholder=','.join(['?'] * (1 + len(detail_data))))
                connection.execute(query, row_data)

    def field_values(self, entry):
        return list(map(lambda x: "" if x is None else str(x),
                        entry[-1 * (self.field_count - 2):]))

    def create_view(self, connection):
        with connection:
            connection.execute("""
              CREATE VIEW {name} AS
                SELECT * FROM entry JOIN {name}_detail USING (id);
            """.format(name=self.name))

    def create_table(self, connection):
        """Create a table for a directives.

        Args:
          connection: A DBAPI-2.0 Connection object.
          entries: A list of directives.
        """
        with connection:
            columns_text = ','.join(self.columns.strip().splitlines())
            connection.execute("""
              CREATE TABLE {name}_detail (
                id 			INTEGER PRIMARY KEY,
                {columns}
              );
            """.format(name=self.name,
                       columns=columns_text))

    def get_detail(self, entry):
        """Provide data to store for details table.

        Args:
          entry: An instance of the desired directive.
        Returns:
          A tuple of the values corresponding to the columns declared in the
          'columns' attribute.
        """
        raise NotImplementedError
