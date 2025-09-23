# Regex_phone_number_validation.py

import re
from time import sleep
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama


def validate_phone_number(phone_number):
    """
    Validate international phone numbers using E.164 format:
    - Optional leading '+'
    - Must start with digits 1-9 (no leading zero)
    - Total length: 8 to 15 digits
    """
    pattern = r'^\+?[1-9]\d{7,14}$'
    return bool(re.fullmatch(pattern, phone_number))


# Edge cases for testing/debugging
valid_cases = [
    "+14155552671",     # Valid US number
    "+250788123456",    # Valid Rwanda number
]

invalid_cases = [
    "123",              # Too short
    "0123456789",       # Starts with 0
    "++250788123456",   # Double '+'
    "+250 788 123 456", # Spaces not allowed
    "+250-788-123-456", # Dashes not allowed
]

# Interactive mode only runs when executed directly
if __name__ == "__main__":
    print(Fore.CYAN + "Welcome to the Phone Number Validation App!")
    sleep(1)
    print(Fore.CYAN + "Validating international phone numbers made easy.")
    sleep(1)

    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Let's validate your phone number.")

    while True:
        user_phone_number = input(Fore.CYAN + "Enter your phone number: ").strip()
        if validate_phone_number(user_phone_number):
            print(Fore.GREEN + "Valid phone number.")
        else:
            print(Fore.RED + "Invalid phone number.")

        continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another phone number? (yes/no): ").strip().lower()
        if continue_choice == 'no':
            print(Fore.CYAN + f"Thank you {user_name}, for using the Phone Number Validation App. Goodbye!")
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
            if validate_phone_number(case):
                print(Fore.GREEN + f"Edge Case Passed: {case} is valid as expected.")
            else:
                print(Fore.RED + f"Edge Case Failed: {case} should be valid.")
            sleep(0.5)

        for case in invalid_cases:
            print(Fore.YELLOW + f"Testing invalid case: {case}")
            sleep(0.5)
            if not validate_phone_number(case):
                print(Fore.GREEN + f"Edge Case Passed: {case} is invalid as expected.")
            else:
                print(Fore.RED + f"Edge Case Failed: {case} should be invalid.")
            sleep(0.5)
    print(Fore.CYAN + "\nExiting the Phone Number Validation App. Have a great day!")   

# End of the phone number validation app