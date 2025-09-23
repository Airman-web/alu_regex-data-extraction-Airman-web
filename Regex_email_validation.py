# Regex_email_validation.py

import re
from time import sleep
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama

def validate_email(email):
    """
    Validates an email address using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$'
    return bool(re.fullmatch(pattern, email))


# Edge cases for testing/debugging
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

# Interactive mode only runs when executed directly
if __name__ == "__main__":
    print(Fore.CYAN + "Welcome to the Email Validation App!")
    sleep(1)
    print(Fore.CYAN + "Validating email addresses made easy.")
    sleep(1)

    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Let's validate your email address.")

    while True:
        user_email = input(Fore.CYAN + "Enter your email address: ").strip()
        if validate_email(user_email):
            print(Fore.GREEN + "Valid email address.")
        else:
            print(Fore.RED + "Invalid email address.")

        continue_choice = input(Fore.LIGHTBLACK_EX + "Do you want to validate another email? (yes/no): ").strip().lower()
        if continue_choice == 'no':
            print(Fore.BLUE + f"Thank you {user_name}, for using the email validation app.")
            sleep(1)
            print(Fore.GREEN + "Exiting the email validation app......")
            sleep(2)
            print(Fore.GREEN + "Successfully exited the email validation app")
            break
        elif continue_choice != 'yes':
            print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")

    # Debug mode for edge cases
    debug = True  # set to False when submitting final version
    if debug:
        print(Fore.YELLOW + "\n--- Debug Mode: Testing Edge Cases ---")
        sleep(1)
        for case in edge_cases:
            print(Fore.YELLOW + f"Testing edge case: {case}")
            sleep(0.5)
            if validate_email(case):
                print(Fore.RED + f"Edge Case Failed: {case} should be invalid.")
            else:
                print(Fore.GREEN + f"Edge Case Passed: {case} is invalid as expected.")
            sleep(0.5)
    print(Fore.CYAN + "\nExiting the Email Validation App. Have a great day!")  

# End of the email validation app
