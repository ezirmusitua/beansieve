from typing import List

from beansieve.lib.entry.Entry import Entry


class Entries(object):
    def __init__(self, entries: List[Entry]):
        self._entries = [Entry(entry) for entry in entries]

    def __iter__(self):
        return iter(self._entries)
