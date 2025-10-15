import logging, sys
from .config import settings

def get_logger(name: str = None):
    logger = logging.getLogger(name or settings.SERVICE_NAME)
    if not logger.handlers:
        h = logging.StreamHandler(sys.stdout)
        fmt = logging.Formatter('%%(asctime)s %%(levelname)s %%(name)s %%(message)s')
        h.setFormatter(fmt)
        logger.addHandler(h)
        logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))
    return logger
