import logging
import traceback
import json
import os
from datetime import datetime

class Log:

    def __init__(self):
        logging.basicConfig(filename='logs.log', level=logging.DEBUG)
        self.shared_instance = logging

    def info(self, file, reference, event):
        data = { 'date': datetime.today(),
                'type' : 'info',
                'info': reference,
                'event' : event }
        self.shared_instance.info(data)

    def debug(self, reference):
        data = { 'date': datetime.today(),
                'type' : 'debug',
                'info': reference}
        self.shared_instance.debug(data)

    def warning(self, byFile, line, reference, error):
        data = { 'date': datetime.today(),
                'type' : 'warning',
                'file' : byFile,
                'info': reference,
                'line' : line,
                'error' : error }
        self.shared_instance.warning(data)

    def critical(self, error):
        exc_type, exc_value, exc_traceback = error
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        data = { 'date' : datetime.today(),
                'type' : 'critical',
                'error': ''.join('!! ' + line for line in lines)}
        self.shared_instance.critical(data)