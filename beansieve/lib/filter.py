from typing import List, Tuple


def split_rules(_rules: str):
    def _split_rule(r: str) -> Tuple[str, str]:
        parts = r.split(":")
        if len(parts) != 2:
            raise Exception("Invalid rule")
        return (parts[0], parts[1])
    rules = list(map(_split_rule, _rules.split(",")))
    return rules


def append_default_rule(_rules: List[Tuple[str, str]]):
    rules = [*_rules]
    rules.append(("$other", "*"))
    return rules


def filter(source: str, dest: str, _rules: str):
    rules = split_rules(_rules)
    rules = append_default_rule(rules)
    pass
