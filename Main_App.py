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

    print(Fore.MAGENTA + "\nWelcome to the REGEX Onboarding Hackathon App!")
    sleep(1)
    print(Fore.MAGENTA + "Choose the type of validation you want to perform:")
    sleep(1)
    print(Fore.MAGENTA + "---------------------------------------------")
    print(Fore.BLUE + "Menu")
    print(Fore.MAGENTA + "---------------------------------------------")   
    print(Fore.MAGENTA + "1. Email Validation")
    print(Fore.MAGENTA + "2. Phone Number Validation")
    print(Fore.MAGENTA + "3. Credit Card Validation")
    print(Fore.MAGENTA + "4. Time Validation (12-hour / 24-hour)")
    print(Fore.MAGENTA + "Q. Quit")
    sleep(1)

    choice = input(Fore.CYAN + "Enter your choice (1/2/3/4 or Q to quit): ").strip().lower()

    if choice == '1':
        print(Fore.CYAN + "You chose Email Validation.")
        sleep(1)
        user_email = input(Fore.CYAN + "Enter your email address: ").strip()
        if validate_email(user_email):
            print(Fore.GREEN + "Valid email address.")
        else:
            print(Fore.RED + "Invalid email address.")

    elif choice == '2':
        print(Fore.CYAN + "You chose Phone Number Validation.")
        sleep(1)
        user_phone_number = input(Fore.CYAN + "Enter your phone number: ").strip()
        if validate_phone_number(user_phone_number):
            print(Fore.GREEN + "Valid phone number.")
        else:
            print(Fore.RED + "Invalid phone number.")

    elif choice == '3':
        print(Fore.CYAN + "You chose Credit Card Validation.")
        sleep(1)
        user_credit_card = input(Fore.CYAN + "Enter your credit card number: ").strip()
        if validate_credit_card(user_credit_card):
            print(Fore.GREEN + "Valid credit card number.")
        else:
            print(Fore.RED + "Invalid credit card number.")

    elif choice == '4':
        print(Fore.CYAN + "You chose Time Validation.")
        sleep(1)
        user_time = input(Fore.CYAN + "Enter time (12-hour or 24-hour format): ").strip()
        if validate_time(user_time):
            print(Fore.GREEN + "Valid time format.")
        else:
            print(Fore.RED + "Invalid time format.")

    elif choice == 'q':
        print(Fore.CYAN + "Thank you for using the REGEX Onboarding Hackathon App. Goodbye!")
        return

    else:
        print(Fore.RED + "Invalid choice. Please restart the app and choose a valid option.")
        sleep(1)
        return

    # Ask user if they want to perform another validation
    while True:
        continue_choice = input(Fore.LIGHTBLACK_EX + "\nDo you want to perform another validation? (yes/no): ").strip().lower()
        if continue_choice == 'yes':
            main()  # Restart the main function
            break
        elif continue_choice == 'no':
            print(Fore.CYAN + "Thank you for using the REGEX Onboarding Hackathon App. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
