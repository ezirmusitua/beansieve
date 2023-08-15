from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class QueryWriter(DirectiveWriter):
    type = data.Query

    columns = """
      name                VARCHAR
      query_string        VARCHAR
    """

    def get_detail(self, entry):
        return (entry.name,
                entry.query_string)
