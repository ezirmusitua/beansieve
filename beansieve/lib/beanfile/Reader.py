from beancount import loader

from beansieve.lib.beanfile.Option import Option
from beansieve.lib.entry import Entries


class BeancountFileReader(object):
    @staticmethod
    def read(entrypoint: str):
        entries, _, option_map = loader.load_file(entrypoint)
        return Entries(entries), Option(option_map)
