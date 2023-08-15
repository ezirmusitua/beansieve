from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class DocumentWriter(DirectiveWriter):
    type = data.Document

    columns = """
      account             VARCHAR
      filenam             VARCHAR
    """

    def get_detail(self, entry):
        return (entry.account,
                entry.filename)
