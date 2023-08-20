from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class NoteWriter(DirectiveWriter):
    type = data.Note

    columns = """
      account             VARCHAR
      comment             VARCHAR
    """

    def get_detail(self, entry):
        return (entry.account,
                entry.comment)
