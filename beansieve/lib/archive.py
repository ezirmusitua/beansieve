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


def archive(source: str, dest: str, period: str):
    raise Exception("Not implemented")
