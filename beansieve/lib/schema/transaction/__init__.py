from typing import Any, List


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


def to_cost_string(posting):
    cost_number = posting[6]
    cost_currency = empty_if_none(posting[7])
    cost_date = empty_if_none(posting[8])
    cost_label = empty_if_none(posting[9])
    out = ""
    if cost_number is not None:
        out = f"{cost_number} {cost_currency}"
    if cost_date != "":
        out = out + (", " if out else "") + cost_date
    if cost_label != "":
        out = out + (", " if out else "") + cost_label
    if out:
        return "{ " + out + " }"
    return ""


def to_price_string(posting):
    price_number = posting[10]
    price_currency = posting[11]
    if price_number is not None:
        return f"@ {price_number} {price_currency}"
    return ""


def to_posting_string(posting: List[Any]):
    flag = empty_if_none(posting[2])
    account = empty_if_none(posting[3])
    number = ensure_float_fixed(posting[4])
    currency = empty_if_none(posting[5])
    return " ".join([
        flag,
        account,
        number,
        currency,
        to_cost_string(posting),
        to_price_string(posting)
    ])

from .TransactionWriter import Transaction
