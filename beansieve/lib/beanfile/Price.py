from .Writer import BeanfileWriter


class PriceWriter(BeanfileWriter):
    def directive_content(self):
        return f"price {self._entry.currency} {self._entry.amount.number} {self._entry.amount.currency}"
