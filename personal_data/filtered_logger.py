#!/usr/bin/env python3
"""
filtered_logger

function filter_datum that returns the log message obfuscated
"""

import re
from typing import List
import logging
import os
import mysql.connector
import datetime

PII_FIELDS = ("name", "email", "password", "phone", "ssn")


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
        return filter_datum(
            self.fields, self.REDACTION, log_message, self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """Obfuscate certain fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*',
        lambda match: match.group(1) + '=' + redaction,
        message
    )


def get_logger() -> logging.Logger:
    """Logger named 'user_data'."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to the MySQL database using environment variables."""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    # Create a connection to the MySQL database
    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return db


def main():
    """Retrieve all rows in the users table and
    display each row in a filtered format."""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()

    # Retrieve all rows in the users table
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    # Display each row in a filtered format
    for row in rows:
        filtered_row = filter_datum(
            PII_FIELDS, RedactingFormatter.REDACTION, str(row), ";"
            )
        logger.info(
            "[HOLBERTON] user_data INFO %s: %s;",
            str(datetime.datetime.now()), filtered_row
            )

    # Display filtered fields
    logger.info("Filtered fields:\n%s", "\n".join(PII_FIELDS))

    cursor.close()
    db.close()
