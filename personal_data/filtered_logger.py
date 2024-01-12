#!/usr/bin/env python3
"""
filtered_logger

function filter_datum that returns the log message obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate certain fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*',
        lambda match: match.group(1) + '=' + redaction,
        message
    )
