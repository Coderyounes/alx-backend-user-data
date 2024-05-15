#!/bin/usr/env python3
""" function redact PII """
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


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
