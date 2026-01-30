# -----------------------------------------------------------------------------
# logger.py - Logging configuration
# Author: Roxanne Prajapati
# Description:
#      Logging setup for monitoring and debugging.
# -----------------------------------------------------------------------------
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger():
    '''
    Create and return the application logger.

    :return: Configured logger instance.
    '''
    logger_obj = logging.getLogger('exchange')
    if logger_obj.handlers:
        return logger_obj

    logger_obj.setLevel(logging.INFO)

    Path('logs').mkdir(exist_ok=True)

    file_handler = RotatingFileHandler(
        'logs/app.log', maxBytes=200_000, backupCount=3, encoding='utf-8'
    )
    file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))

    logger_obj.addHandler(file_handler)
    logger_obj.addHandler(console_handler)

    return logger_obj
