from Regex_email_validation import validate_email                  # Import the email validation function
from Regex_phone_number_validation import validate_phone_number    # Import the phone number validation function
from Regex_credit_card_validation import validate_credit_card      # Import the credit card validation function
from colorama import Fore, init         # Import colorama for colored text
from time import sleep                  # Import sleep function to add delays

init(autoreset=True)  # Initialize colorama with autoreset


def handle_email_validation():
    """Handle user input for email validation."""
    print(Fore.CYAN + "You chose Email Validation.")
    sleep(1)
    user_email = input(Fore.CYAN + "Enter your email address: ").strip()
    if validate_email(user_email):
        print(Fore.GREEN + "Valid email address.")
    else:
        print(Fore.RED + "Invalid email address.")


def handle_phone_validation():
    """Handle user input for phone number validation."""
    print(Fore.CYAN + "You chose Phone Number Validation.")
    sleep(1)
    user_phone_number = input(Fore.CYAN + "Enter your phone number (digits only): ").strip()
    if validate_phone_number(user_phone_number):
        print(Fore.GREEN + "Valid phone number.")
    else:
        print(Fore.RED + "Invalid phone number.")


def handle_credit_card_validation():
    """Handle user input for credit card validation."""
    print(Fore.CYAN + "You chose Credit Card Validation.")
    sleep(1)
    user_credit_card = input(Fore.CYAN + "Enter your credit card number: ").strip()
    if validate_credit_card(user_credit_card):
        print(Fore.GREEN + "Valid credit card number.")
    else:
        print(Fore.RED + "Invalid credit card number.")


def main():
    """
    Main menu for the REGEX Onboarding Hackathon App.
    Allows users to validate email addresses, phone numbers,
    and credit card numbers using regex.
    """
    print(Fore.MAGENTA + "Welcome to the REGEX Onboarding Hackathon App!")

    while True:  # Loop until user quits
        sleep(1)
        print(Fore.MAGENTA + "\nChoose the type of validation you want to perform:")
        print(Fore.MAGENTA + "---------------------------------------------")
        print(Fore.BLUE + "Menu")
        print(Fore.MAGENTA + "---------------------------------------------")   
        print(Fore.MAGENTA + "1. Email Validation")
        print(Fore.MAGENTA + "2. Phone Number Validation")
        print(Fore.MAGENTA + "3. Credit Card Validation")
        print(Fore.MAGENTA + "q. Quit")
        
        choice = input(Fore.CYAN + "Enter your choice (1/2/3/q): ").strip()

        if choice == '1':
            handle_email_validation()
        elif choice == '2':
            handle_phone_validation()
        elif choice == '3':
            handle_credit_card_validation()
        elif choice.lower() == 'q':
            print(Fore.CYAN + "Thank you for using the REGEX Onboarding Hackathon App. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please choose 1, 2, 3, or q.")


if __name__ == "__main__":
    main()
    
# End of Main_App.py