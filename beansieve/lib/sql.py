"""Convert a Beancount ledger into an SQL database.
"""
__copyright__ = "Copyright (C) 2014-2017  Martin Blais"
__license__ = "GNU GPLv2"

import logging
import sys

from beancount import loader
from beancount.utils import misc_utils

from beansieve.lib.Transaction import Transaction

from .Database import connect_db
from .Entry import Entry
from .Transaction import Transaction
from .directives import directives


def convert_to_sqlite(source: str, dest: str):
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s: %(message)s')

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
