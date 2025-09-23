# Regex_email_validation.py

import re
from colorama import Fore, init
from time import sleep

init(autoreset=True)

# Email validation function
def validate_email(email):
    pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$'
    return bool(re.fullmatch(pattern, email))

# Edge cases for email
edge_cases = [
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@com",
    "username@domain..com",
    "username@domain.c",
    "username@-domain.com",
    "username@domain-.com",
]

# Function to run email edge-case tests
def run_email_edge_cases():
    print(Fore.YELLOW + "\n--- Running Edge-Case Tests for Email ---")
    while True:
        user_input = input(Fore.CYAN + "Enter an email to test (or press Enter to skip): ").strip()
        if user_input:
            result = validate_email(user_input)
            print(Fore.GREEN + f"Your Input '{user_input}': Valid" if result else Fore.RED + f"Your Input '{user_input}': Invalid")
        for case in edge_cases:
            result = validate_email(case)
            print(Fore.GREEN + f"Edge Case '{case}': Valid" if result else Fore.RED + f"Edge Case '{case}': Invalid")
        print(Fore.YELLOW + "--- Finished Edge-Case Tests for Email ---\n")
        cont = input(Fore.LIGHTBLACK_EX + "Run another email edge test? (yes/no): ").strip().lower()
        if cont != 'yes':
            break
