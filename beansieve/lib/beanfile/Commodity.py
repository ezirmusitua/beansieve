from .Writer import BeanfileWriter


class CommodityWriter(BeanfileWriter):
    def directive_content(self):
        return f"commodity {self._entry.currency}"
