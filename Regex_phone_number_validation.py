"""
    Validate international phone numbers using E.164 format:
    - Optional leading '+'
    - Must start with digits 1-9 (no leading zero)
    - Total length: 8 to 15 digits
    """

# Import necessary libraries
from time import sleep                 # Import sleep function to add delays
from colorama import Fore, init       # Import colorama for colored text
import re                           # Import the regex module
init(autoreset=True)                  # Initialize colorama with autoreset

# Welcome message
print(Fore.CYAN + "Welcome to the Phone Number Validation App!")
sleep(1)
print(Fore.CYAN + "Validating international phone numbers made easy.")
sleep(1)

user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Let's validate your phone number.")

# Phone number validation function
def validate_phone_number(phone_number):
    # International format (E.164 standard)
    pattern = r'^\+?[1-9]\d{7,14}$'
    # Explanation of the regex pattern:
    # ^\+?                : Optional '+' at the start
    # [1-9]              : First digit must be between 1-9 (no leading zero)
    # \d{7,14}          : Followed by 7 to 14 digits
    # $                  : End of the string
    return bool(re.fullmatch(pattern, phone_number))     # Use re.fullmatch to check if the phone number matches the pattern

# First input
user_phone_number = input("Enter your phone number: ")
if validate_phone_number(user_phone_number):
    print(Fore.GREEN + "Valid phone number.")
else:
    print(Fore.RED + "Invalid phone number.")

# Edge cases
valid_cases = [
    "+14155552671",     # Valid US number
    "+250788123456",    # Valid Rwanda number
]

invalid_cases = [
    "123",              # Too short
    "0123456789",       # Starts with 0 (invalid in E.164)
    "++250788123456",   # Double +
    "+250 788 123 456", # Spaces not allowed
    "+250-788-123-456", # Dashes not allowed
]

print(Fore.YELLOW + "\n--- Testing Edge Cases ---")

# Check valid cases
for case in valid_cases:
    if validate_phone_number(case):
        print(Fore.GREEN + f"Edge case '{case}' is valid as expected.")
    else:
        print(Fore.RED + f"Edge case '{case}' FAILED: should be valid.")

# Check invalid cases
for case in invalid_cases:
    if not validate_phone_number(case):
        print(Fore.GREEN + f"Edge case '{case}' is invalid as expected.")
    else:
        print(Fore.RED + f"Edge case '{case}' FAILED: should be invalid.")

# Loop to allow user to validate multiple phone numbers
while True:
    continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another phone number? (yes/no): ").strip().lower()
    if continue_choice == 'yes':
        user_phone_number = input(Fore.CYAN + "Enter your phone number: ").strip()
        sleep(1)
        if validate_phone_number(user_phone_number):
            print(Fore.GREEN + "Valid phone number.")
        else:
            print(Fore.RED + "Invalid phone number.")
    elif continue_choice == 'no':
        print(Fore.CYAN + "Thank you for using the Phone Number Validation App. Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")



# Debug mode
debug = True  # set to False when submitting final version
if debug:
    print(Fore.YELLOW + "\n--- Debug Mode: Re-testing Edge Cases ---")
    sleep(1)

    for case in valid_cases:
        print(Fore.YELLOW + f"Testing valid case: {case}")
        sleep(0.5)
        if validate_phone_number(case):
            print(Fore.GREEN + f"Edge Case Passed: {case} is valid as expected.")
            sleep(0.5)
        else:
            print(Fore.RED + f"Edge Case Failed: {case} should be valid.")
            sleep(0.5)

    for case in invalid_cases:
        print(Fore.YELLOW + f"Testing invalid case: {case}")
        sleep(0.5)
        if not validate_phone_number(case):
            print(Fore.GREEN + f"Edge Case Passed: {case} is invalid as expected.")
            sleep(0.5)
        else:
            print(Fore.RED + f"Edge Case Failed: {case} should be invalid.")
            sleep(0.5)  
print(Fore.BLUE +  f"Thank you {user_name}, for using the email validation app.")
print(Fore.CYAN + "\nExiting the Phone Number Validation App. Have a great day!")

# End of the phone number validation app