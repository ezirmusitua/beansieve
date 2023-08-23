from beansieve.lib.aggregate import aggregate
from beansieve.lib.archive import archive
from beansieve.lib.commands import parse


if __name__ == '__main__':
    args = parse()
    if args.type == "archive":
        archive(args.source, args.dest, args.keep)
    elif args.type == "aggregate":
        aggregate(args.source, args.dest, args.rule)
    else:
        print("Invalid type")
