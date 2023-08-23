import re
from typing import Any, Pattern


from beansieve.lib.beanfile import BeanfileWriterFactory
from beansieve.lib.predicate import account_name_like, date_less_than_today, type_is


class Entry(object):
    def __init__(self, entry: Any):
        self._entry = entry

    def __eq__(self, other: str | Pattern):
        if type(other) is str:
            return type_is(self._entry, other)
        if isinstance(other, re.Pattern):
            return account_name_like(self._entry, other)
        raise Exception("Unsupported comparison")

    def __ne__(self, other: str | Pattern):
        return not (self == other)

    def __lt__(self, period):
        return date_less_than_today(self._entry, period)

    def write(self):
        writer = BeanfileWriterFactory.create(self._entry)
        return writer.build()
