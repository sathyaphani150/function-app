import os


class Config:
    ENV = os.getenv("ENV", "dev")
    APP_NAME = os.getenv("APP_NAME", "TaskMonitorFunctionApp")