import logging


def init_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)-8s: %(message)s'
    )
