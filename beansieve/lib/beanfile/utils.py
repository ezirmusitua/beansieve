from pathlib import Path
from typing import List

from beansieve.lib.entry.Entry import Entry
from beansieve.lib.beanfile.Option import Option


def build_beancount_content(entries: List[Entry]):
    return "\n".join([entry.write() for entry in entries])


def write_beancount(dest: str, key: str, entries: List[Entry]):
    key_dest = Path(dest).joinpath(f"{key}.beancount")
    content = build_beancount_content(entries)
    key_dest.write_text(content, encoding="utf-8")


def write_main_beancount(
    dest: str,
    key: str,
    option: Option,
    includes: List[str],
    entries: List[Entry]
):
    main_dest = Path(dest).joinpath(f"{key}.beancount")
    includes_string = "\n".join(
        [f"include \"./{name}.beancount\"" for name in includes])
    entries_string = build_beancount_content(entries)
    content = option.to_beancount(
    ) + f"\n\n{includes_string}\n\n{entries_string}"
    main_dest.write_text(content)
