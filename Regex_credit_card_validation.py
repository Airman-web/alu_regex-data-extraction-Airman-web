# Regex_credit_card_validation.py

import re
from time import sleep
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama


def validate_credit_card(card_number):
    """
    Validate credit card numbers:
    - Accepts 16-digit numbers in formats:
        1234567890123456
        1234 5678 9012 3456
        1234-5678-9012-3456
    """
    pattern = r'^(?:\d{4}[- ]?){3}\d{4}$'
    return bool(re.fullmatch(pattern, card_number))


# Edge cases for testing/debugging
valid_cases = [
    "1234567890123456",        # Plain digits
    "1234 5678 9012 3456",     # Spaces
    "1234-5678-9012-3456",     # Dashes
]

invalid_cases = [
    "123456789012345",          # Too short
    "12345678901234567",        # Too long
    "1234_5678_9012_3456",      # Underscores not allowed
    "1234 5678 9012-3456",      # Mixed separators not allowed
    "abcd efgh ijkl mnop",      # Letters
]

# Interactive mode only runs when executed directly
if __name__ == "__main__":
    print(Fore.CYAN + "Welcome to the Credit Card Validation App!")
    sleep(1)
    print(Fore.CYAN + "Validating credit card numbers made easy.")
    sleep(1)

    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Let's validate your credit card number.")

    while True:
        user_credit_card = input(Fore.CYAN + "Enter your credit card number: ").strip()
        if validate_credit_card(user_credit_card):
            print(Fore.GREEN + "Valid credit card number.")
        else:
            print(Fore.RED + "Invalid credit card number.")

        continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another credit card? (yes/no): ").strip().lower()
        if continue_choice == 'no':
            print(Fore.CYAN + f"Thank you {user_name}, for using the Credit Card Validation App. Goodbye!")
            break
        elif continue_choice != 'yes':
            print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")

    # Debug mode for edge cases
    debug = True  # set to False when submitting final version
    if debug:
        print(Fore.YELLOW + "\n--- Debug Mode: Testing Edge Cases ---")
        sleep(1)
        for case in valid_cases:
            print(Fore.YELLOW + f"Testing valid case: {case}")
            sleep(0.5)
            if validate_credit_card(case):
                print(Fore.GREEN + f"Edge Case Passed: {case} is valid as expected.")
            else:
                print(Fore.RED + f"Edge Case Failed: {case} should be valid.")
            sleep(0.5)

        for case in invalid_cases:
            print(Fore.YELLOW + f"Testing invalid case: {case}")
            sleep(0.5)
            if not validate_credit_card(case):
                print(Fore.GREEN + f"Edge Case Passed: {case} is invalid as expected.")
            else:
                print(Fore.RED + f"Edge Case Failed: {case} should be invalid.")
            sleep(0.5)
    print(Fore.CYAN + "\nExiting the Credit Card Validation App. Have a great day!")

# End of the credit card validation app
