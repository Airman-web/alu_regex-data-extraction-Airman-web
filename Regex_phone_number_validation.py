#Import neccessary libraries for better user experience
from time import sleep                           # Import sleep function to add delays
from colorama import Fore, Style, init           # Import colorama for colored text
init(autoreset=True)                            # Initialize colorama with autoreset

#Welcome to the phone number validation app
print(Fore.CYAN + "Welcome to the Phone Number Validation App!")
sleep(1)  # Pause for 1 second  to enhance user experience
print(Fore.CYAN + "Validating phone numbers made easy.")
sleep(1)  # Pause for 1 second to enhance user experience

user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Let's validate your phone number.")

# Phone number validation using regex
import re                              # Import the regex module
def validate_phone_number(phone_number):
    # Define the regex pattern for a valid phone number
    pattern = r'^\+?1?\s*(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$'
   
    # Explanation of the regex pattern:
    # ^\+?1?\s*                   : Matches an optional '+' sign, optional '1' country code, followed by optional spaces
    # (?:\(\d{3}\)|\d{3})         : Matches area code in parentheses or as three digits
    # [\s.-]?                     : Matches an optional separator (space, dot, or hyphen)
    # \d{3}                       : Matches the next three digits
    # [\s.-]?                     : Matches another optional separator (space, dot, or hyphen)
    # \d{4}                       : Matches the last four digits
    # $                           : End of the string  
   
   
    # Use re.fullmatch to check if the phone number matches the pattern
    if re.fullmatch(pattern, phone_number):
        return True
    else:
        return False
# Test the function to validate a phone number
user_phone_number = input("Enter your phone number: ")
if validate_phone_number(user_phone_number):
    print(Fore.GREEN + "Valid phone number.")
else:
    print(Fore.RED + "Invalid phone number.")       


# Error handling for invalid phone number formats with Edge cases
edge_cases = [
    "123456",                     # Too short
    "123-45-6789",                # Incorrect format
    "(123)456-789",               # Missing digit
    "123.4567.890",               # Incorrect format
    "+1 (123 456-7890",           # Missing closing parenthesis
    "1-800-FLOWERS",              # Alphanumeric
    "++1 (123) 456-7890",         # Double plus sign
]
for case in edge_cases:
    if validate_phone_number(case):
        print(Fore.GREEN + f"Edge case '{case}' is incorrectly marked as valid.")
    else:
        print(Fore.RED + f"Edge case '{case}' is correctly marked as invalid.")
    if validate_phone_number(user_phone_number = input("Enter your phone number: ")
):
        print(Fore.GREEN + "Valid email address.")
    else:
        print(Fore.RED + "Invalid email address.")
        print(Fore.GREEN + "Valid email address.")
        print(Fore.RED + "Invalid email address.")
        print(Fore.RED + "Invalid email address.")  

    
# Loop to exit app by user input if they don't want to continue with a new phone number validation
while True:
    continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another phone number? (yes/no): ").strip().lower()
    if continue_choice == 'yes':
        user_phone_number = input(Fore.CYAN + "Enter your phone number: ").strip()
        sleep(1)  # Pause for 1 second to enhance user experience
        if validate_phone_number(user_phone_number):
            print(Fore.GREEN + "Valid phone number.")
        else:
            print(Fore.RED + "Invalid phone number.")
    elif continue_choice == 'no':
        print(Fore.BLUE +  f"Thank you {user_name}, for using the phone number validation app.")
        sleep(1)  # Pause for 1 second to enhance user experience
        print(Fore.GREEN + "Exiting the phone number validation app......")
        sleep(2)  # Pause for 2 seconds before exiting
        print(Fore.GREEN + "Successfully exited the phone number validation app")

        break
    else:
        print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")
        print(Fore.GREEN + f"Edge case '{case}' is incorrectly marked as valid.")
        print(Fore.RED + f"Edge case '{case}' is correctly marked as invalid.")
        print(Fore.GREEN + f"Edge case '{case}' is incorrectly marked as valid.")
        
        