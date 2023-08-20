from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class BalanceWriter(DirectiveWriter):
    type = data.Balance

    columns = """
      account             VARCHAR
      amount_number       DECIMAL(16,6)
      amount_currency     CHARACTER(10)
      diff_number         DECIMAL(16,6)
      diff_currency       CHARACTER(10)
    """

    def get_detail(self, entry):
        return (entry.account,
                entry.amount.number,
                entry.amount.currency,
                entry.diff_amount.currency if entry.diff_amount else None,
                entry.diff_amount.currency if entry.diff_amount else None)
