import re
from typing import Pattern, Tuple

from beansieve.lib.beanfile.Reader import BeancountFileReader
from beansieve.lib.fs import mkdir
from beansieve.lib.structure import Structure


RULE_SEP = ","
KV_SEP = "|"


def split_rules(_rules: str):
    def _split_rule(r: str) -> Tuple[str, Pattern[str]]:
        parts = r.split(KV_SEP)
        if len(parts) != 2:
            raise Exception("Invalid rule")
        return (parts[0], re.compile(parts[1]))
    rules = list(map(_split_rule, _rules.split(RULE_SEP)))
    return rules


def match_rule(entry, rules):
    for (name, pattern) in rules:
        if entry == pattern:
            return name
    return None


def aggregate(source: str, dest: str, _rules: str):
    mkdir(dest)
    rules = split_rules(_rules)
    entries, option = BeancountFileReader.read(source)
    structure = Structure(dest, option)

    for entry in entries:
        if entry != "transaction":
            structure.append(entry)
            continue
        key = match_rule(entry, rules)
        if key is None:
            structure.append_main(entry)
        else:
            structure.append(entry, key)

    structure.write()
