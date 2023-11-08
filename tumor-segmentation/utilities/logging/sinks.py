import logging
import sys
from typing import Any

from loguru import logger
from utilities.logging.formatters import single_line_format


def add_terminal_sink(logger: logger):
    """
    Adds a log sink with the terminal as the destination.
    """
    logger.add(sys.stdout, level=logging.DEBUG, format=single_line_format)


def add_file_sink(logger: logger, filename="emily.log", rotation="5 MB"):
    """
    Adds a log sink with a file as the destination.
    By default, the log file is rotated with a max file size of 5 MB.
    """
    logger.add(filename, level=logging.DEBUG,
               format=single_line_format, rotation=rotation)


def add_custom_sink(logger: logger, sink: Any):
    """
    Adds a log sink with an arbitrary function handler as the destination.
    The sink handler as provided with a raw log record.
    See https://loguru.readthedocs.io/en/stable/api/logger.html#the-record-dict
    for details on the contents of a raw log record.
    """
    # In Loguru, a log message is simply a string with a special
    # property (message.record) that contains all contextual information
    # for custom processing of a log record.
    logger.add(lambda message: sink(message.record), level=logging.DEBUG)
