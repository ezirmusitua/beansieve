from .Writer import BeanfileWriter


class OpenWriter(BeanfileWriter):
    def directive_content(self):
        currencies = ",".join(self._entry.currencies or [])
        booking = ""
        if self._entry.booking:
            booking = str(self._entry.booking).split(".")[1]
        return f"open {self._entry.account} {currencies} \"{booking}\""
