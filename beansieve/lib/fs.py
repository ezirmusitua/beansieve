from pathlib import Path
from typing import List


def mkdir(_target: str, subs: List[str] = list()):
    target = Path(_target)
    if not target.exists():
        target.mkdir()
    for sub in subs:
        target.joinpath(sub).mkdir()
