from sqlite3.dbapi2 import Connection

from .database import connect_db

ENTRY_TABLE_SQL = """CREATE TABLE entry (
    id 			        INTEGER PRIMARY KEY,
    date 		        DATE,
    type                CHARACTER(8),
    source_filename	    STRING,
    source_lineno	    INTEGER,
    directive           VARCHAR
);
"""


def create_table(connection: Connection):
    with connection:
        connection.execute(ENTRY_TABLE_SQL)


if __name__ == '__main__':
    connection = connect_db(".artifacts/example.sqlite")
    create_table(connection)
