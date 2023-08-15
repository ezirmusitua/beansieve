from decimal import Decimal
import sqlite3 as dbapi


def adapt_decimal(number):
    """Adapt a Decimal instance to a string for creating queries.

    Args:
      number: An instance of Decimal.
    Returns:
      A string.
    """
    return str(number)


def convert_decimal(string):
    """Convert a Decimal string to a Decimal instance.

    Args:
      string: A decimal number in a string.
    Returns:
      An instance of Decimal.
    """
    return Decimal(string)


def setup_decimal_support():
    """Setup sqlite3 to support conversions to/from Decimal numbers.
    """
    dbapi.register_adapter(Decimal, adapt_decimal)
    dbapi.register_converter("decimal", convert_decimal)


def connect_db(path: str):
    # The only supported DBAPI-2.0 backend for now is SQLite3.
    connection = dbapi.connect(path)
    setup_decimal_support()
    return connection
