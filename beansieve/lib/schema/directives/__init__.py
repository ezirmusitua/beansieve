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

directives = [
    BalanceWriter(),
    CloseWriter(),
    CommodityWriter(),
    DocumentWriter(),
    EventWriter(),
    NoteWriter(),
    OpenWriter(),
    PadWriter(),
    PriceWriter(),
    QueryWriter()
]
