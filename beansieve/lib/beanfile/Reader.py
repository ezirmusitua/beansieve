from beancount import loader

from ..Entries import Entries
from .Option import Option


class BeancountFileReader(object):
    @staticmethod
    def read(entrypoint: str):
        entries, _, option_map = loader.load_file(entrypoint)
        return Entries(entries), Option(option_map)
