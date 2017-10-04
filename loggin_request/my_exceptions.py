import logger

class CustomError(Exception):
    __log = logger.Log()
    def __init__(self, message, error):
        self.message = message
        self.__fill_logger(error)

    def __fill_logger(self, error):
        self.__log.critical(error)


class AnotherError(CustomError):
    def __init__(self, description, message):
        self.message = message
        self.description = description

class Error404(CustomError):
    def __init__(self, url, attribute, message):
        self.url = url
        self.attribute = attribute
        self.message = message

class RequestError(CustomError):
    def __init__(self, url, attribute, error):
        self.url = url
        self.attribute = attribute
        self.message = error