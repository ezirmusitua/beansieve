import re
from typing import Any

from beancount.core import data as BeancountEntries
from beansieve.lib.beanfile import BeanfileWriterFactory


class Entry(object):

    def __init__(self, entry: Any):
        self._entry = entry

    def test_date(self, predicate):
        return predicate(self._entry.date)

    def test_account(self, pattern):
        if not isinstance(self._entry, BeancountEntries.Transaction):
            return False
        for posting in self._entry.postings:
            if re.match(pattern, posting.account):
                return True
        return False

    def to_sql(self, connection):
        pass

    def to_beancount(self):
        writer = BeanfileWriterFactory.create(self._entry)
        return writer.build()

    @staticmethod
    def from_beancount(entry):
        return Entry(entry)

    @staticmethod
    def from_sqlite():
        pass
