from .Writer import BeanfileWriter


class CloseWriter(BeanfileWriter):
    def directive_content(self):
        return f"close {self._entry.account}"
