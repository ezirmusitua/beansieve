from datetime import date as Date, timedelta

from beansieve.lib.beanfile.Reader import BeancountFileReader
from beansieve.lib.beanfile.utils import write_beancount, write_main_beancount
from beansieve.lib.fs import mkdir

DefaultDirectiveMapping = [
    {"directives": ["open", "balance", "pad", "close"], "name": "account"},
    {"directives": ["commodity"], "name": "commodity"},
    {"directives": ["event"], "name": "event"},
    {"directives": ["document"], "name": "document"},
    {"directives": ["note"], "name": "note"},
    {"directives": ["query"], "name": "query"},
    {"directives": ["price"], "name": "price"}
]


def get_timedelta(period: str):
    if period.endswith("d"):
        return timedelta(days=int(period[:-1]))
    if period.endswith("w"):
        return timedelta(days=int(period[:-1]) * 7)
    if period.endswith("m"):
        return timedelta(days=int(period[:-1]) * 30)
    raise Exception(f"Invalid period {period}")


def archive(source: str, dest: str, period: str):
    mkdir(dest)
    now = Date.today()

    def should_archive(x: Date): return x < now - get_timedelta(period)

    archived_book = list()
    main_book = list()
    entries, option = BeancountFileReader.read(source)

    for entry in entries:
        if entry.test_date(should_archive):
            archived_book.append(entry)
        else:
            main_book.append(entry)

    write_beancount(dest, "Archived", archived_book)
    write_main_beancount(dest, "Main", option, ["Archived"], main_book)
