# Regex_credit_card_validation.py

import re
from colorama import Fore, init
from time import sleep

init(autoreset=True)

# Credit card validation function
def validate_credit_card(card):
    # Accepts format: "1234 5678 9012 3456", "1234-5678-9012-3456", or "1234567890123456"
    pattern = r'^(?:\d{4}[- ]?){3}\d{4}$'
    return bool(re.fullmatch(pattern, card))

# Edge cases for credit card
edge_cases = [
    "1234 5678 9012 3456",  # Valid
    "1234-5678-9012-3456",  # Valid
    "1234567890123456",      # Valid
    "1234_5678_9012_3456",  # Invalid
]

# Function to run credit card edge-case tests
def run_credit_card_edge_cases():
    print(Fore.YELLOW + "\n--- Running Edge-Case Tests for Credit Card ---")
    while True:
        user_input = input(Fore.CYAN + "Enter a credit card number to test (or press Enter to skip): ").strip()
        if user_input:
            result = validate_credit_card(user_input)
            print(Fore.GREEN + f"Your Input '{user_input}': Valid" if result else Fore.RED + f"Your Input '{user_input}': Invalid")
        for case in edge_cases:
            result = validate_credit_card(case)
            print(Fore.GREEN + f"Edge Case '{case}': Valid" if result else Fore.RED + f"Edge Case '{case}': Invalid")
        print(Fore.YELLOW + "--- Finished Edge-Case Tests for Credit Card ---\n")
        cont = input(Fore.LIGHTBLACK_EX + "Run another credit card edge test? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

