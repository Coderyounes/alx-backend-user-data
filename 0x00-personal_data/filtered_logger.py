#!/usr/bin/env python3
""" function redact PII """
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        :param fields: fields need to redacted
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        :param record: record format to fill
        :return: redacted data
        """
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger():
    logger = logging.getLogger("user_data")
    logging.basicConfig(level=logging.INFO)
    stream_handler = RedactingFormatter(list(PII_FIELDS))
    logging.StreamHandler()
    # TODO: adjust loging level to INFO
    # TODO: logger should have StreamHandler with Redacting Formatter class as formatter
    return logger


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    :param fields: List of sensitive parameter
    :param redaction: redaction word
    :param message: whole message
    :param separator: separator to handle with
    :return: redacted message
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
