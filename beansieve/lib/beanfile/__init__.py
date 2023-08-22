from beancount.core import data as BeancountEntryTypes


from .Balance import BalanceWriter
from .Close import CloseWriter
from .Commodity import CommodityWriter
from .Custom import CustomWriter
from .Document import DocumentWriter
from .Event import EventWriter
from .Note import NoteWriter
from .Open import OpenWriter
from .Pad import PadWriter
from .Price import PriceWriter
from .Query import QueryWriter
from .Transaction import TransactionWriter
from .Writer import BeanfileWriter


class BeanfileWriterFactory(object):
    @staticmethod
    def create(entry) -> BeanfileWriter:
        if isinstance(entry, BeancountEntryTypes.Balance):
            return BalanceWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Close):
            return CloseWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Commodity):
            return CommodityWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Document):
            return DocumentWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Event):
            return EventWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Note):
            return NoteWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Open):
            return OpenWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Pad):
            return PadWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Price):
            return PriceWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Query):
            return QueryWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Transaction):
            return TransactionWriter(entry)
        elif isinstance(entry, BeancountEntryTypes.Custom):
            return CustomWriter(entry)
        else:
            raise Exception(
                f"{type(entry).__name__} Writer not implemented: ", entry)
