import os
from os import path

from beancount.parser import version


def parse():
    parser = version.ArgumentParser(description=__doc__)
    parser.add_argument("--type", help="<aggregate|archive>")
    parser.add_argument("--source", help="input beancount file")
    parser.add_argument("--dest", help="output")
    parser.add_argument("--keep", help="keep period entries in main file")
    parser.add_argument("--rule", help="rule use to filter")

    args = parser.parse_args()
    if not path.exists(args.source):
        raise FileNotFoundError("Source not exists")
    # Delete dest if existed.
    if path.exists(args.dest):
        os.remove(args.dest)

    return args
