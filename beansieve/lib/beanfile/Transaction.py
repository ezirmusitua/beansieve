from datetime import date
from typing import Any, List

from .Writer import BeanfileWriter


def empty_if_none(val):
    return "" if val is None else str(val)


def ensure_float_fixed(val: float):
    if val is None:
        return ""
    if isinstance(val, int):
        return str(val) + ".00"
    if isinstance(val, float) and val.is_integer():
        return str(val) + ".00"
    return str(val)


def cost(posting):
    if posting.cost is None:
        return ""
    cost_number = posting.cost.number
    cost_currency = posting.cost.currency
    cost_date = posting.cost.date.strftime(
        "%Y-%m-%d") if posting.cost.date else ""
    cost_label = posting.cost.label or ""
    out = f"{cost_number} {cost_currency}"
    if cost_date != "":
        out = out + (", " if out else "") + cost_date
    if cost_label != "":
        out = out + (", " if out else "") + cost_label
    if out:
        return "{ " + out + " }"
    return ""


def price(posting):
    if posting.price is None:
        return ""
    return f"@ {str(posting.price)}"


def build_posting(posting):
    parts = filter(lambda x: bool(x), [
        posting.flag,
        posting.account,
        str(posting.units),
        cost(posting),
        price(posting)
    ])
    return " ".join(parts)


def tags(entry):
    return " ".join(list(map(lambda x: f"#{x}", (entry.tags or ()))))


def links(entry):
    return " ".join(list(map(lambda x: f"^{x}", (entry.links or ()))))


class TransactionWriter(BeanfileWriter):
    def directive_content(self):
        return f"{self._entry.flag} \"{empty_if_none(self._entry.payee)}\" " + \
            f"\"{self._entry.narration}\" {tags(self._entry)} {links(self._entry)}\n"

    def multiline_content(self):
        out = list()
        for posting in self._entry.postings:
            out.append(f"\t{build_posting(posting)}")
        return "\n".join(out)
