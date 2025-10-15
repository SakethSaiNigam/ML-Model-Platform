import os

class Settings:
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/artifacts/model.pkl")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    SERVICE_NAME: str = os.getenv("SERVICE_NAME", "capgemini-rt-ml-platform")

settings = Settings()
