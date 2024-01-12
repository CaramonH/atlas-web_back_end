#!/usr/bin/env python3
"""
filtered_logger

function filter_datum that returns the log message obfuscated
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate certain fields in a log message."""
    pattern = f'(?<={separator}){"|".join(fields)}(?={separator})'
    return re.sub(pattern, redaction, message)
