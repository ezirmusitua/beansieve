from .Writer import BeanfileWriter


class QueryWriter(BeanfileWriter):
    def directive_content(self):
        return f"query {self._entry.query_string}"
