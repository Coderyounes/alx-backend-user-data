#!/bin/usr/env python3
""" function redact PII """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
