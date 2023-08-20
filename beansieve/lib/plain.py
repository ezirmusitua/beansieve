from pathlib import Path
from .database import connect_db
from .schema.transaction import Transaction
from .schema.directives import (
    BalanceWriter,
    CloseWriter,
    CommodityWriter,
    DocumentWriter,
    EventWriter,
    NoteWriter,
    OpenWriter,
    PadWriter,
    PriceWriter,
    QueryWriter,
)


def convert_to_plain(source: str, dest: str):
    connection = connect_db(source)
    dest_file = Path(dest)

    balances = BalanceWriter().to_plain(connection)
    closes = CloseWriter().to_plain(connection)
    commodities = CommodityWriter().to_plain(connection)
    documents = DocumentWriter().to_plain(connection)
    events = EventWriter().to_plain(connection)
    notes = NoteWriter().to_plain(connection)
    opens = OpenWriter().to_plain(connection)
    pads = PadWriter().to_plain(connection)
    prices = PriceWriter().to_plain(connection)
    queries = QueryWriter().to_plain(connection)
    transactions = Transaction().to_plain(connection)
    dest_file.write_text(
        "\n".join([balances, closes, commodities, documents, events,
                   notes, opens, pads, prices, queries, transactions]),
        encoding="utf-8"
    )

    pass
