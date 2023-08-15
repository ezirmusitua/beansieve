from .lib.sql import convert_to_sqlite
from .lib.plain import convert_to_plain
from .lib.commands import parse


if __name__ == '__main__':
    args = parse()
    if args.type == "sql":
        convert_to_sqlite(args.source, args.dest)
    else:
        convert_to_plain(args.source, args.dest)
