from beancount.core import data

from .DirectiveWriter import DirectiveWriter


class CommodityWriter(DirectiveWriter):
    """
    2004-01-26 commodity VHT
      export: "NYSEARCA:VHT"
      name: "Vanguard Health Care ETF"
      price: "USD:google/NYSEARCA:VHT"
    """
    type = data.Commodity

    columns = """
        currency         VARCHAR 
        export           VARCHAR
        name             VARCHAR
        price            VARCHAR
    """

    def get_detail(self, entry):
        return (
            entry.currency,
            entry.meta.get("export", None),
            entry.meta.get("name", None),
            entry.meta.get("price", None)
        )

    def field_values(self, entry):
        out = [entry[5]]
        if entry[6] is not None:
            out.append(f"\n\texport: \"{entry[6]}\"")
        if entry[7] is not None:
            out.append(f"\n\tname: \"{entry[7]}\"")
        if entry[8] is not None:
            out.append(f"\n\tprice: \"{entry[8]}\"")
        return out
