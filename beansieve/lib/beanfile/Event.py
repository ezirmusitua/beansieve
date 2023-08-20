from .Writer import BeanfileWriter


class EventWriter(BeanfileWriter):
    def directive_content(self):
        return f"event \"{self._entry.type}\" \"{self._entry.description}\""
