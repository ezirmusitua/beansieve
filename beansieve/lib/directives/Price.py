from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class PriceWriter(DirectiveWriter):
    type = data.Price

    columns = """
      currency            CHARACTER(10)
      amount_number       DECIMAL(16,6)
      amount_currency     CHARACTER(10)
    """

    def get_detail(self, entry):
        return (entry.currency,
                entry.amount.number,
                entry.amount.currency)
