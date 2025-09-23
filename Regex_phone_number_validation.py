# Regex_phone_number_validation.py
import re

PHONE_EDGE_CASES = [
    "123",                # Too short
    "0123456789",         # Starts with 0
    "++250788123456",     # Double +
    "+250 788 123 456",   # Spaces
    "+250-788-123-456",   # Dashes
]

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate international phone numbers (E.164 format).
    """
    pattern = r'^\+?[1-9]\d{7,14}$'
    return bool(re.fullmatch(pattern, phone_number))
