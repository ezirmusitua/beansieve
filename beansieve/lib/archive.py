import json
from pathlib import Path
from typing import List

DefaultDirectiveMapping = [
    {"directives": ["open", "balance", "pad", "close"], "name": "account"},
    {"directives": ["commodity"], "name": "commodity"},
    {"directives": ["event"], "name": "event"},
    {"directives": ["document"], "name": "document"},
    {"directives": ["note"], "name": "note"},
    {"directives": ["query"], "name": "query"},
    {"directives": ["price"], "name": "price"}
]


class ArchiveRule(object):
    def __init__(self, fp: str):
        self._fp = fp
        self._data = json.loads(Path(fp).read_text(encoding="utf-8"))

    @property
    def folders(self):
        return self._data.get("folders", [])

    @property
    def period(self):
        return self._data.get("period", "y").lower()

    @property
    def directives(self):
        return self._data.get("directives", DefaultDirectiveMapping)


def prepare_folders(dest: str, directives: List[str], ):
    _dest = Path(dest)
    if not _dest.exists():
        _dest.mkdir()
    for directive in directives:
        _dest.joinpath(directive).mkdir()


def archive(source: str, dest: str, rule_fp: str):
    rule = ArchiveRule(rule_fp)
    for directive in rule.directives:
        print("->1",)
    for folder in rule.folders:
        print(folder)
