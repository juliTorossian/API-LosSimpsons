import logging
import os
import traceback
from enum import Enum

class LoggerTypes(Enum):
    ERROR       = "error"
    CRITICAL    = "critical"
    DEBUG       = "debug"
    INFO        = "info"
    WARNING     = "warning"
    LOG         = "log"
    EXCEPTION   = "exception"

class Logger():

    def __set_logger(self):
        log_directory = 'src/utils/log'
        log_filename = 'app.log'

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)

            if (level == LoggerTypes.CRITICAL):
                logger.critical(message)
            elif (level == LoggerTypes.DEBUG):
                logger.debug(message)
            elif (level == LoggerTypes.ERROR):
                logger.error(message)
            elif (level == LoggerTypes.INFO):
                logger.info(message)
            elif (level == LoggerTypes.WARNING):
                logger.warning(message)
            elif (level == LoggerTypes.LOG):
                logger.log(message)
            elif (level == LoggerTypes.EXCEPTION):
                logger.exception(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)