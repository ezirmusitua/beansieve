import re
from beancount.core import data as BeancountEntries
from typing import NamedTuple, Any

from beansieve.lib.beanfile import BeanfileWriterFactory


class Entry(object):

    def __init__(self, entry: Any):
        self._entry = entry

    @property
    def date(self):
        return self._entry.date

    @property
    def meta(self):
        return self._entry.meta

    @property
    def account(self):
        return self._entry.account

    def to_sql(self, connection):
        pass

    def to_beancount(self):
        writer = BeanfileWriterFactory.create(self._entry)
        return writer.build()

    def test(self, pattern, field="posting_account"):
        if field == "posting_account" and not isinstance(self._entry, BeancountEntries.Transaction):
            return False
        for posting in self._entry.postings:
            if re.match(pattern, posting.account):
                return True

        return False

    @staticmethod
    def from_beancount(entry):
        return Entry(entry)

    @staticmethod
    def from_sqlite():
        pass
