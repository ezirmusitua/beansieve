from beancount.core import data as BeancountEntries

from .Balance import BalanceWriter
from .Close import CloseWriter
from .Commodity import CommodityWriter
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
        if isinstance(entry, BeancountEntries.Balance):
            return BalanceWriter(entry)
        elif isinstance(entry, BeancountEntries.Close):
            return CloseWriter(entry)
        elif isinstance(entry, BeancountEntries.Commodity):
            return CommodityWriter(entry)
        elif isinstance(entry, BeancountEntries.Document):
            return DocumentWriter(entry)
        elif isinstance(entry, BeancountEntries.Event):
            return EventWriter(entry)
        elif isinstance(entry, BeancountEntries.Note):
            return NoteWriter(entry)
        elif isinstance(entry, BeancountEntries.Open):
            return OpenWriter(entry)
        elif isinstance(entry, BeancountEntries.Pad):
            return PadWriter(entry)
        elif isinstance(entry, BeancountEntries.Price):
            return PriceWriter(entry)
        elif isinstance(entry, BeancountEntries.Query):
            return QueryWriter(entry)
        elif isinstance(entry, BeancountEntries.Transaction):
            return TransactionWriter(entry)
        else:
            raise Exception("Writer not implemented")
