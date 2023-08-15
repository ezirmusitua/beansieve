import os
from os import path

from beancount.parser import version


def parse():
    parser = version.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--type", help="convert to `sql` or convert to `plain`")
    parser.add_argument("--source", help="Beancount input filename")
    parser.add_argument("--dest", help="Filename of database file to create")

    args = parser.parse_args()
    if not path.exists(args.source):
        raise FileNotFoundError("Source not exists")
    # Delete previous database if it already exists.
    if path.exists(args.dest):
        os.remove(args.dest)

    return args
