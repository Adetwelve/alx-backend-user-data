#!/usr/bin/env python3
""" A funtion that return log message obfuscated """
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """ Regex-ing replace occurance certain field value """
    return re.sub(rf"({'|'.join(map(re.escape, fields))})=[^;]+",
                  rf"\1={redaction}", message)
