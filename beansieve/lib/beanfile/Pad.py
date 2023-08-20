from .Writer import BeanfileWriter


class PadWriter(BeanfileWriter):
    def directive_content(self):
        return f"pad {self._entry.account} {self._entry.source_account}"
