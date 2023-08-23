from beansieve.lib.predicate import type_is


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

WriterMapping = dict(
    balance=BalanceWriter,
    close=CloseWriter,
    commodity=CommodityWriter,
    custom=CustomWriter,
    document=DocumentWriter,
    event=EventWriter,
    note=NoteWriter,
    open=OpenWriter,
    pad=PadWriter,
    price=PriceWriter,
    query=QueryWriter,
    transaction=TransactionWriter
)


class BeanfileWriterFactory(object):
    @staticmethod
    def create(entry) -> BeanfileWriter:
        for type, cls in WriterMapping.items():
            if type_is(entry, type):
                return cls(entry)
        raise Exception(f"Writer not implemented for ", entry)
