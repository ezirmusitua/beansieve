from .Writer import BeanfileWriter


class BalanceWriter(BeanfileWriter):
    def directive_content(self):
        return f"balance {self._entry.account} {self._entry.amount.number} {self._entry.amount.currency} " + \
            f"{self._entry.diff_amount.currency if self._entry.diff_amount else ''}" + \
            f"{self._entry.diff_amount.currency if self._entry.diff_amount else ''}"
