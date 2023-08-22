from typing import Dict, List, Tuple

from .Entry import Entry
from .beanfile.Reader import BeancountFileReader
from .beanfile.utils import write_beancount, write_main_beancount
from .fs import mkdir


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


def aggregate(source: str, dest: str, _rules: str):
    mkdir(dest)
    rules = split_rules(_rules)
    key_entries: Dict[str, List[Entry]] = {name: list() for (name, _) in rules}
    main_entries = list()
    entries, option = BeancountFileReader.read(source)

    for entry in entries:
        to_key = "Main"
        for (name, pattern) in rules:
            matched = entry.test_account(pattern)
            if (matched):
                to_key = name
                break
        if to_key == "Main":
            main_entries.append(entry)
        else:
            key_entries[to_key].append(entry)

    for (key, entries) in key_entries.items():
        write_beancount(dest, key, entries)

    write_main_beancount(dest, "Main", option, list(
        key_entries.keys()), main_entries)
