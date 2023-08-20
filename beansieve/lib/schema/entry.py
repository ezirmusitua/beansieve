

class Entry(object):

    def to_sql(self, connection, entries):
        self.create_table(connection)

    def create_table(self, connection):
        """Create a table of common data for all entries.

        Args:
          connection: A DBAPI-2.0 Connection object.
          entries: A list of directives.
        """
        with connection:
            connection.execute("""
              CREATE TABLE entry (
                id 			    INTEGER PRIMARY KEY,
                date 		    DATE,
                type            CHARACTER(8),
                source_filename	STRING,
                source_lineno	INTEGER
              );
            """)
