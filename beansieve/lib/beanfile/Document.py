from .Writer import BeanfileWriter


class DocumentWriter(BeanfileWriter):
    def directive_content(self):
        return f"document {self._entry.account}  {self._entry.filename}"
