from .lib.aggregate import aggregate
from .lib.archive import archive
from .lib.commands import parse
from .lib.logging import init_logging
from .lib.sql import convert_to_sqlite

init_logging()

if __name__ == '__main__':
    args = parse()
    if args.type == "archive":
        archive(args.source, args.dest, args.keep)
    elif args.type == "aggregate":
        aggregate(args.source, args.dest, args.rule)
    elif args.type == "sql":
        convert_to_sqlite(args.source, args.dest)
    else:
        print("Invalid type")
