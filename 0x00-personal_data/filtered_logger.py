#!/bin/usr/env python3
""" function redact PII """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return: redacted message
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
