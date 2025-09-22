#Import neccessary libraries for better user experience
from time import sleep                           # Import sleep function to add delays
from colorama import Fore, Style, init           # Import colorama for colored text
init(autoreset=True)                            # Initialize colorama with autoreset

#Welcome to the email validation app
print(Fore.CYAN + "Welcome to the Email Validation App!")
sleep(1)  # Pause for 1 second  to enhance user experience
print(Fore.CYAN + "Validating email addresses made easy.")
sleep(1)  # Pause for 1 second to enhance user experience

user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Let's validate your email address.")

# Email vaildation using regex
import re                              # Import the regex module
def validate_email(email):
    # Define the regex pattern for a valid email address
    pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$'
   
    # Explanation of the regex pattern:
    # ^(?!.*\.\.)                : Ensures no consecutive dots in the email
    # [a-zA-Z0-9._%+-]+          : Matches the local part of the email (before the @)
    # @                           : Matches the '@' symbol
    # [A-Za-z0-9]+(?:-[A-Za-z0-9]+)* : Matches the domain name (before the first dot), allowing hyphens but not starting or ending with them
    # (\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+ : Matches the top-level domain(s), allowing hyphens but not starting or ending with them
    # $                           : End of the string  
   
   
    # Use re.fullmatch to check if the email matches the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

# Test the function to validate an email address
user_email = input("Enter your email address: ")
if validate_email(user_email):
    print(Fore.GREEN + "Valid email address.")
else:
    print(Fore.RED + "Invalid email address.")

# Error handling for invalid email formats with Edge cases
edge_cases = [
    "plainaddress",                # Missing '@' and domain
    "@missingusername.com",        # Missing username
    "username@.com",               # Missing domain name
    "username@com",                # Missing top-level domain
    "username@domain..com",        # Double dot in domain
    "username@domain.c",           # Single character top-level domain
    "username@-domain.com",        # Domain starts with a hyphen
    "username@domain-.com",        # Domain ends with a hyphen
]

# Loop to exit app by user input if they don't want to continue with a new email validation
while True:
    continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another email? (yes/no): ").strip().lower()
    if continue_choice == 'yes':
        user_email = input(Fore.CYAN + "Enter your email address: ").strip()
        sleep(1)  # Pause for 1 second to enhance user experience
        if validate_email(user_email):
            print(Fore.GREEN + "Valid email address.")
        else:
            print(Fore.RED + "Invalid email address.")
    elif continue_choice == 'no':
        print(Fore.BLUE +  f"Thank you {user_name}, for using the email validation app.")
        sleep(1)  # Pause for 1 second to enhance user experience
        print(Fore.GREEN + "Exiting the email validation app......")
        sleep(2)  # Pause for 2 seconds before exiting
        print(Fore.GREEN + "Successfully exited the email validation app")

        break
    else:
        print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")


     # Placeholder for future edge cases

debug = True  # set to False when submitting final version

if debug:
    for case in edge_cases:
        debug_info = f"Testing edge case: {case}"
        print(Fore.YELLOW + debug_info)
        sleep(0.5)
        if validate_email(case):
            print(Fore.RED + f"Edge Case Failed: {case} should be invalid.")
        else:
            print(Fore.GREEN + f"Edge Case Passed: {case} is invalid as expected.") 
        sleep(0.5)
# End of the email validation app