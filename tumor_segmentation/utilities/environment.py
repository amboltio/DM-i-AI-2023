from pydantic_settings import BaseSettings
from argparse import ArgumentParser
from utilities.singleton import singleton

@singleton
class Environment(BaseSettings):
    ENVIRONMENT: str = 'production'
    HOST_IP: str
    CONTAINER_PORT: int
