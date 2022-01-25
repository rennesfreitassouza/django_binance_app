import logging
from django.conf import settings


class Log():
    """Log class """

    _logs_basicConfig = logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] - %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %z', level=settings.LOGGING_LEVEL)

    def __init__(self, name=None):
        self._log = logging.getLogger(f'cs_logger.{name}')

    def set_debug_msg(self, msg):
        self._log.debug(msg)

    def set_info_msg(self, msg):
        self._log.info(msg)

    def set_warning_msg(self, msg):
        self._log.warning(msg)

    def set_error_msg(self, msg):
        self._log.error(msg)

    def set_critical_msg(self, msg):
        self._log.critical(msg)
