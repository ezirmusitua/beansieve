from pathlib import Path
from typing import List
from beansieve.lib.beanfile.Option import Option
from beansieve.lib.predicate import type_is
from beansieve.lib.entry.Entry import Entry


def build_beancount_content(entries: List[Entry]):
    return "\n".join([entry.write() for entry in entries])


class Structure(object):
    def __init__(self, dest: str, option: Option):
        self._dest = dest
        self._option = option
        self._main = list()
        self._named = dict(
            account=list(),
            commodity=list(),
            custom=list(),
            document=list(),
            event=list(),
            note=list(),
            price=list(),
            query=list(),
            history=list(),
        )

    def append_main(self, entry):
        self._main.append(entry)

    def append(self, entry, key=None):
        if key is not None:
            self._append_to(key, entry)
            return
        if entry == "open" or entry == "close":
            self._append_to("account", entry)
        if entry == "commodity":
            self._append_to("commodity", entry)
        if entry == "custom":
            self._append_to("custom", entry)
        if entry == "document":
            self._append_to("document", entry)
        if entry == "event":
            self._append_to("event", entry)
        if entry == "note":
            self._append_to("note", entry)
        if entry == "price":
            self._append_to("price", entry)
        if entry == "query":
            self._append_to("query", entry)
        if entry == "transaction":
            self._append_to("history", entry)

    def _append_to(self, key: str, entry):
        if self._named.get(key, None) is None:
            self._named[key] = list()
        self._named[key].append(entry)

    def write(self):
        for (key, entries) in self._named.items():
            key_dest = Path(self._dest).joinpath(f"{key}.beancount")
            content = build_beancount_content(entries)
            key_dest.write_text(content, encoding="utf-8")
        main_dest = Path(self._dest).joinpath(f"main.beancount")
        includes_string = "\n".join(
            [f"include \"./{name}.beancount\"" for name in self._named.keys()])
        entries_string = build_beancount_content(self._main)
        content = self._option.to_beancount(
        ) + f"\n\n{includes_string}\n\n{entries_string}"
        main_dest.write_text(content)
