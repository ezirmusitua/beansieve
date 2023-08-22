from sqlite3.dbapi2 import Connection
from typing import List


from .Entry import Entry


class Entries(object):
    def __init__(self, entries: List[Entry]):
        self._entries = [Entry.from_beancount(entry) for entry in entries]

    def __iter__(self):
        return iter(self._entries)

    @staticmethod
    def from_sqlite(connection: Connection):
        pass
