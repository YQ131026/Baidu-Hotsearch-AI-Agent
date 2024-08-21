import logging
from config.settings import LOG_FILE_PATH

class Logger:
    def __init__(self):
        logging.basicConfig(
            filename=LOG_FILE_PATH,
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(message)s'
        )
        self.logger = logging.getLogger()

    def log(self, message):
        self.logger.info(message)

