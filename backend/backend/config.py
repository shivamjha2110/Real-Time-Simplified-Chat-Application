import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Chat App"
    PROJECT_VERSION: str = "1.0.0"
    WEBSOCKET_PATH: str = "/ws"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

settings = Settings()
