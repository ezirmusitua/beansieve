import re
from typing import Pattern

from .type import TypeIs


class AccountNameLike(object):
    def __call__(self, entry, pattern: Pattern[str]):
        type_is = TypeIs()
        if type_is(entry, "event"):
            return False
        if type_is(entry, "price"):
            return False
        if type_is(entry, "query"):
            return False
        if type_is(entry, "custom"):
            return False
        if type_is(entry, "commodity"):
            return False
        if type_is(entry, "transaction"):
            for posting in entry.postings:
                if re.match(pattern, posting.account) is not None:
                    return True
            return False
        return re.match(pattern, entry.account) is not None
