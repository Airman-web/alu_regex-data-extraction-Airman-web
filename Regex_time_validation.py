# Regex_time_validation.py

import re
from time import sleep
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama


def validate_time(time_str):
    """
    Validate time in 12-hour or 24-hour format:
    - 24-hour: HH:MM (00:00 to 23:59)
    - 12-hour: H:MM AM/PM or HH:MM AM/PM
    """
    # 24-hour format regex
    pattern_24 = r'^(?:[01]\d|2[0-3]):[0-5]\d$'
    
    # 12-hour format regex
    pattern_12 = r'^(0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM|am|pm)$'
    
    return bool(re.fullmatch(pattern_24, time_str) or re.fullmatch(pattern_12, time_str))


# Edge cases for testing/debugging
valid_cases = [
    "14:30",     # 24-hour format
    "2:30 PM",   # 12-hour format
    "02:05 am",  # 12-hour with leading zero and lowercase
    "00:00",     # Midnight 24-hour
    "12:59 PM",  # Noon 12-hour
]

invalid_cases = [
    "24:00",     # Invalid hour in 24-hour
    "13:60",     # Invalid minute
    "0:30 PM",   # Invalid 12-hour (should be 12 or 1-12)
    "12:30 XM",  # Invalid AM/PM
    "1230",      # Missing colon
]

# Interactive mode only runs when executed directly
if __name__ == "__main__":
    print(Fore.CYAN + "Welcome to the Time Validation App!")
    sleep(1)
    print(Fore.CYAN + "Validate 12-hour and 24-hour time formats easily.")
    sleep(1)

    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Let's validate some time entries.")

    while True:
        user_time = input(Fore.CYAN + "Enter time (12-hour or 24-hour format): ").strip()
        if validate_time(user_time):
            print(Fore.GREEN + "Valid time format.")
        else:
            print(Fore.RED + "Invalid time format.")

        continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another time? (yes/no): ").strip().lower()
        if continue_choice == 'no':
            print(Fore.CYAN + f"Thank you {user_name}, for using the Time Validation App. Goodbye!")
            break
        elif continue_choice != 'yes':
            print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")

    # Debug mode for edge cases
    debug = True
    if debug:
        print(Fore.YELLOW + "\n--- Debug Mode: Testing Edge Cases ---")
        sleep(1)
        for case in valid_cases:
            print(Fore.YELLOW + f"Testing valid case: {case}")
            sleep(0.5)
            if validate_time(case):
                print(Fore.GREEN + f"Edge Case Passed: {case} is valid as expected.")
            else:
                print(Fore.RED + f"Edge Case Failed: {case} should be valid.")
            sleep(0.5)

        for case in invalid_cases:
            print(Fore.YELLOW + f"Testing invalid case: {case}")
            sleep(0.5)
            if not validate_time(case):
                print(Fore.GREEN + f"Edge Case Passed: {case} is invalid as expected.")
            else:
                print(Fore.RED + f"Edge Case Failed: {case} should be invalid.")
            sleep(0.5)
    print(Fore.CYAN + "\nExiting the Time Validation App. Have a great day!")

# End of the time validation app
