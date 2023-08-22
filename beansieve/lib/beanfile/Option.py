"""
_references:: https://beancount.github.io/docs/beancount_options_reference.html
"""

from typing import Any, Dict

from beancount.core.data import Booking

_EXCLUDED_KEYS = [
    "commodities",
    "dcontext",
    "documents",
    "filename",
    "include",
    "input_hash",
    "plugin"
]


def convert_option_value(value: Any):
    if value is None:
        return ""
    elif type(value) is bool:
        return str(value).upper()
    elif type(value) is dict:
        return " ".join([f"{key}:{val}" for (key, val) in value.items()])
    elif type(value) is list:
        return " ".join([f"{item}" for item in value])
    elif isinstance(value, Booking):
        return str(value).split(".")[1]
    else:
        return str(value)


class Option(object):
    """
    option "operating_currency"               "CNY"
    plugin "beancount.plugins.auto_accounts"
    plugin "beancount.plugins.forecast"
    plugin "beancount.plugins.check_closing"
    plugin "beancount.plugins.sellgains"
    """

    def __init__(self, option_map: Dict[str, Any]):
        self._option_map = option_map

    def to_beancount(self):
        lines = list()
        for (key, val) in self._option_map.items():
            if key in _EXCLUDED_KEYS:
                continue
            value = convert_option_value(val)
            if value == "":
                continue
            lines.append(f"option \"{key}\" \"{value}\"")
        for (name, value) in self._option_map.get("plugin", []):
            lines.append(f"plugin \"{name}\" {convert_option_value(value)}")
        return "\n".join(lines)
