#!/usr/bin/env python3
"""
filtered_logger

function filter_datum that returns the log message obfuscated
"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format log record by redacting specified fields """
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """Obfuscate certain fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*',
        lambda match: match.group(1) + '=' + redaction,
        message
    )
