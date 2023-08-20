from sqlite3.dbapi2 import Connection
from typing import List

from beancount import loader

from .Entry import Entry


class Entries(object):
    def __init__(self, entries: List[Entry]):
        self._entries = [Entry.from_beancount(entry) for entry in entries]

    def __iter__(self):
        return iter(self._entries)

    @staticmethod
    def from_sqlite(connection: Connection):
        pass

    @staticmethod
    def from_beancount(beancount_file: str):
        entries, _, __ = loader.load_file(beancount_file)
        return Entries(entries)
