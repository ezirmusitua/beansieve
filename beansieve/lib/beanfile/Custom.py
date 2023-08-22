from beancount.parser.grammar import ValueType
from .Writer import BeanfileWriter


class CustomWriter(BeanfileWriter):
    """
    Example: 
    2016-06-01 custom "budget" Expenses:Food "monthly" 3000.00 CNY
    """

    def directive_content(self):
        def values(vs: ValueType):
            out = list()
            for value in vs:
                if value.dtype is str:
                    out.append(f"\"{value.value}\"")
                else:
                    out.append(str(value.value))
            return " ".join(out)
        return f"custom \"{self._entry.type}\" {values(self._entry.values)}"
