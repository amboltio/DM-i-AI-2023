from loguru import logger
from fastapi import Request, FastAPI
from starlette.responses import JSONResponse


def value_error_exceptions(_: Request, exception: ValueError):
    return JSONResponse(
        status_code=500,
        content={
            'errors': [str(exception), 'Something went wrong.']
        }
    )


def handle_generic_exceptions(request: Request, exception: Exception):
    logger.error('Runtime error', request=request, exception=exception)
    return JSONResponse(
        status_code=500,
        content={
            'errors': [str(exception), 'Something went wrong.']
        }
    )


def configure_exception_handlers(app: FastAPI):
    app.add_exception_handler(
        ValueError, value_error_exceptions
    )
    app.add_exception_handler(
        Exception, handle_generic_exceptions
    )
