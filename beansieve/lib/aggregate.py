from .Entries import Entries
from .Entry import Entry
from .fs import mkdir
from typing import List, Tuple, Dict
from pathlib import Path


RULE_SEP = ","
KV_SEP = "|"


def split_rules(_rules: str):
    def _split_rule(r: str) -> Tuple[str, str]:
        parts = r.split(KV_SEP)
        if len(parts) != 2:
            raise Exception("Invalid rule")
        return (parts[0], parts[1])
    rules = list(map(_split_rule, _rules.split(RULE_SEP)))
    return rules


def build_beancount_content(entries: List[Entry]):
    return "\n".join([entry.to_beancount() for entry in entries])


def aggregate(source: str, dest: str, _rules: str):
    mkdir(dest)
    rules = split_rules(_rules)
    result: Dict[str, List[Entry]] = {name: list() for (name, _) in rules}
    main_file = list()

    for entry in Entries.from_beancount(source):
        to_name = "Main"
        for (name, pattern) in rules:
            matched = entry.test(pattern)
            if (matched):
                to_name = name
                break
        if to_name == "Main":
            main_file.append(entry)
        else:
            result[to_name].append(entry)

    for (key, entries) in result.items():
        key_dest = Path(dest).joinpath(f"{key}.beancount")
        content = build_beancount_content(entries)
        key_dest.write_text(content, encoding="utf-8")

    main_dest = Path(dest).joinpath("Main.beancount")
    includes = "\n".join(
        [f"include \"./{name}.beancount\"" for name in result.keys()])
    content = "option \"operating_currency\" \"USD\"\n\n" + \
        f"{includes}\n\n{build_beancount_content(main_file)}"
    main_dest.write_text(content)
