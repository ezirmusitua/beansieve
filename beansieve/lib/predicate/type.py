from beancount.core import data as BeancountEntryTypes


TypeMapping = dict(
    balance=BeancountEntryTypes.Balance,
    close=BeancountEntryTypes.Close,
    commodity=BeancountEntryTypes.Commodity,
    custom=BeancountEntryTypes.Custom,
    document=BeancountEntryTypes.Document,
    event=BeancountEntryTypes.Event,
    note=BeancountEntryTypes.Note,
    open=BeancountEntryTypes.Open,
    pad=BeancountEntryTypes.Pad,
    price=BeancountEntryTypes.Price,
    query=BeancountEntryTypes.Query,
    transaction=BeancountEntryTypes.Transaction,
)


class TypeIs(object):

    def __call__(self, entry, type: str):
        expected = TypeMapping.get(type, None)
        if expected is None:
            raise Exception("Unexpected beancount data type")
        return isinstance(entry, expected)
