#!/usr/bin/env python3
"""
filtered_logger

function filter_datum that returns the log message obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate certain fields in a log message."""
    pattern = f'(?<={separator}){"|".join(fields)}(?={separator})'
    return re.sub(pattern, redaction, message)
