import logging


class file_logging:
    def __init__(self, uniq_id, endpoint, filepath):
        self.uniq_id = uniq_id
        self.endpoint = endpoint
        self.filepath = filepath

        logger_formatter = "$(asctime)s - $(levelname)s - {%s} [%s] [$(module)s]: $(message)s" % (self.uniq_id, self.endpoint)
        formatter = logging.Formatter((logger_formatter.replace("$", "%")))

        channel = logging.FileHandler(self.filepath)
        channel.setFormatter(formatter)

        file_log = logging.getLogger(self.uniq_id)
        file_log.setLevel(logging.INFO)  # Default as INFO
        file_log.handlers = []           # Reinitiate handler to avoid duplicate log entry.
        file_log.addHandler(channel)
        file_log.propagate=False         # Avoid printing log message to console.

        self.file_log = file_log

    def openfile(self):
        return self.file_log

    def info(self, message):
        self.file_log.setLevel(logging.INFO)
        self.file_log.info(message)

    def warning(self, message):
        self.file_log.setLevel(logging.WARNING)
        self.file_log.warning(message)

    def error(self, message):
        self.file_log.setLevel(logging.ERROR)
        self.file_log.error(message)

    def critical(self, message):
        self.file_log.setLevel(logging.CRITICAL)
        self.file_log.critical(message)

    def debug(self, message):
        self.file_log.setLevel(logging.DEBUG)
        self.file_log.debug(message)

    def closefile(self):
        logging.shutdown()