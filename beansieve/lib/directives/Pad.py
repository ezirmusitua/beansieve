from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class PadWriter(DirectiveWriter):
    type = data.Pad

    columns = """
      account             VARCHAR
      source_account      VARCHAR
    """

    def get_detail(self, entry):
        return (entry.account, entry.source_account)
