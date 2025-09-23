# Regex_time_validation.py
import re

TIME_EDGE_CASES = [
    "14:30",
    "2:30 PM",
    "00:00",
    "12:59 AM",
    "24:00",
    "13:60",
    "0:00 PM"
]

def validate_time(time_str: str) -> bool:
    """
    Validate time in 12-hour or 24-hour format.
    Examples:
        12-hour: 01:45 PM, 12:30 AM
        24-hour: 00:00, 23:59
    """
    # 12-hour format with AM/PM
    pattern_12 = r'^(0?[1-9]|1[0-2]):[0-5][0-9]\s?(AM|PM|am|pm)$'
    # 24-hour format
    pattern_24 = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    return bool(re.fullmatch(pattern_12, time_str) or re.fullmatch(pattern_24, time_str))
