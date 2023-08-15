from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class CloseWriter(DirectiveWriter):
    type = data.Close

    columns = """
      account             VARCHAR
    """

    def get_detail(self, entry):
        return (entry.account,)
