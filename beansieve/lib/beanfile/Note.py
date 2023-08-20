from .Writer import BeanfileWriter


class NoteWriter(BeanfileWriter):
    def directive_content(self):
        return f"note {self._entry.account} {self._entry.commenttext}"
