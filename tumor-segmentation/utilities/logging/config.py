import logging

from fastapi.applications import FastAPI
from loguru import logger
from utilities.logging.handlers import (LoggingIntercepter,
                                        http_request_logging_middleware)
from utilities.logging.sinks import (add_custom_sink, add_file_sink,
                                     add_terminal_sink)


def _clear_default_logging_handlers(prefix=''):
    """
    Clears the handlers for all existing loggers.
    Provide a logger prefix to limit the set of loggers
    to clear handlers for.
    """
    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith(prefix)
    )
    for log in loggers:
        log.handlers = []


def _clear_default_loguru_handlers():
    logger.configure(handlers=[])


def initialize_logging():
    """
    Initializes logging handlers and sinks. New sinks and handlers
    should be registered in this function.
    """

    # Uvicorn is set up with default loggers.
    # We override them here in order to control how, when, and where
    # uvicorn (and all other) logs are handled.
    _clear_default_logging_handlers(prefix='uvicorn.')
    _clear_default_loguru_handlers()

    # Intercept all uvicorn logs so we can process them as we see fit
    logging.getLogger("uvicorn").handlers = [LoggingIntercepter()]

    # All logs emitted by 1) the intercepter and 2) all loguru.logger.* method calls
    # will be sent to a loguru sink. Sinks are simply destinations for logging data.
    # By default, we add two sinks; one for sending logs to the console and to a file.
    # To send logs to a database, e.g. an Elasticsearch instance, simply add a custom
    # sink to send the data there.
    # See https://loguru.readthedocs.io/en/stable/api/logger.html for details.
    add_file_sink(logger)
    add_terminal_sink(logger)

    # Arbitrary sinks to process raw log records (for sending to log databases for example)
    # can be configured as such:
    
    # add_custom_sink(logger, lambda record: print(
    #     f'Received raw log record: {record}'
    # ))


def initialize_logging_middleware(app: FastAPI):
    app.middleware("http")(http_request_logging_middleware)
