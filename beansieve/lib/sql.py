import logging
import sys

from beancount import loader
from beancount.utils import misc_utils

from .database import connect_db
from .schema.directives import directives
from .schema.entry import Entry
from .schema.transaction import Transaction


def convert_to_sqlite(source: str, dest: str):
    entries, _, __ = loader.load_file(
        source,
        log_timings=logging.info,
        log_errors=sys.stderr
    )

    connection = connect_db(dest)

    for part in [Entry(), Transaction(), *directives]:
        step_name = getattr(part, '__name__', part.__class__.__name__)
        with misc_utils.log_time(step_name, logging.info):
            part.to_sql(connection, entries)

    return 0
