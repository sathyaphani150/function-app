import os

class Config:
    API_KEY = os.getenv("API_KEY")
    ENV = os.getenv("ENV", "dev")