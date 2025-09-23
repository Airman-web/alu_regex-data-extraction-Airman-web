# Main_App.py

from Regex_email_validation import validate_email
from Regex_phone_number_validation import validate_phone_number
from Regex_credit_card_validation import validate_credit_card
from Regex_time_validation import validate_time
from colorama import Fore, init
from time import sleep

init(autoreset=True)  # Initialize colorama

def main():
    """
    Main menu for the REGEX Onboarding Hackathon App.
    Allows users to validate email addresses, phone numbers,
    credit card numbers, and time formats using regex.
    """
    while True:
        # Display the menu
        print(Fore.MAGENTA + "\nWelcome to the REGEX Onboarding Hackathon App!")
        sleep(0.5)
        print(Fore.MAGENTA + "Choose the type of validation you want to perform:")
        print(Fore.MAGENTA + "---------------------------------------------")
        print(Fore.BLUE + "Menu")
        print(Fore.MAGENTA + "---------------------------------------------")   
        print(Fore.MAGENTA + "1. Email Validation")
        print(Fore.MAGENTA + "2. Phone Number Validation")
        print(Fore.MAGENTA + "3. Credit Card Validation")
        print(Fore.MAGENTA + "4. Time Validation (12-hour / 24-hour)")
        print(Fore.MAGENTA + "Q. Quit")
        sleep(0.5)

        choice = input(Fore.CYAN + "Enter your choice (1/2/3/4 or Q to quit): ").strip().lower()

        # Email validation
        if choice == '1':
            while True:
                user_email = input(Fore.CYAN + "Enter your email address: ").strip()
                if validate_email(user_email):
                    print(Fore.GREEN + "Valid email address.")
                else:
                    print(Fore.RED + "Invalid email address.")
                retry = input(Fore.LIGHTBLACK_EX + "Do you want to validate another email? (yes/no): ").strip().lower()
                if retry != 'yes':
                    break

        # Phone number validation
        elif choice == '2':
            while True:
                user_phone = input(Fore.CYAN + "Enter your phone number: ").strip()
                if validate_phone_number(user_phone):
                    print(Fore.GREEN + "Valid phone number.")
                else:
                    print(Fore.RED + "Invalid phone number.")
                retry = input(Fore.LIGHTBLACK_EX + "Do you want to validate another phone number? (yes/no): ").strip().lower()
                if retry != 'yes':
                    break

        # Credit card validation
        elif choice == '3':
            while True:
                user_card = input(Fore.CYAN + "Enter your credit card number: ").strip()
                if validate_credit_card(user_card):
                    print(Fore.GREEN + "Valid credit card number.")
                else:
                    print(Fore.RED + "Invalid credit card number.")
                retry = input(Fore.LIGHTBLACK_EX + "Do you want to validate another credit card? (yes/no): ").strip().lower()
                if retry != 'yes':
                    break

        # Time validation
        elif choice == '4':
            while True:
                user_time = input(Fore.CYAN + "Enter time (12-hour or 24-hour format): ").strip()
                if validate_time(user_time):
                    print(Fore.GREEN + "Valid time format.")
                else:
                    print(Fore.RED + "Invalid time format.")
                retry = input(Fore.LIGHTBLACK_EX + "Do you want to validate another time? (yes/no): ").strip().lower()
                if retry != 'yes':
                    break

        # Quit option
        elif choice == 'q':
            print(Fore.CYAN + "Thank you for using the REGEX Onboarding Hackathon App. Goodbye!")
            break

        # Invalid menu option
        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option (1-4 or Q).")
            sleep(0.5)


if __name__ == "__main__":
    main()
