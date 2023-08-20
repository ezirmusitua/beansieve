from .Writer import BeanfileWriter


class OpenWriter(BeanfileWriter):
    def directive_content(self):
        currencies = " ".join(self._entry.currencies or [])
        return f"open {self._entry.account} {currencies}"
