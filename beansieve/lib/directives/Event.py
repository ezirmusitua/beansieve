from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class EventWriter(DirectiveWriter):
    type = data.Event

    columns = """
      type                VARCHAR
      description         VARCHAR
    """

    def get_detail(self, entry):
        return (entry.type,
                entry.description)

    def field_values(self, entry):
        return [f"\"{entry[5]}\"", f"\"{entry[6]}\""]
