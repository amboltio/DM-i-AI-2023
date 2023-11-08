import logging

from fastapi import Request
from loguru import logger
from starlette.responses import Response


class LoggingIntercepter(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


async def http_request_logging_middleware(request: Request, call_next) -> Response:
    """
    Intercepts all HTTP requests and responses to log rudimentary information.
    The request and response objects are assigned to the record.extra dict.
    """
    logger.info(f'HTTP {request.method} for {request.url}', request=request)
    response: Response = await call_next(request)
    logger.info(f'HTTP {response.status_code} for {request.url}',
                request=request, response=response)
    return response
