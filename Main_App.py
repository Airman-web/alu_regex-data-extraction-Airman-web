# Main_App.py

from Regex_email_validation import validate_email
from Regex_phone_number_validation import validate_phone_number
from Regex_credit_card_validation import validate_credit_card
from Regex_time_validation import validate_time
from colorama import Fore, init
from time import sleep

init(autoreset=True)

def run_email_module():
    valid_email_cases = [
        "test@example.com",
        "user.name@domain.co",
        "firstname.lastname@company.co.uk"
    ]
    invalid_email_cases = [
        "plainaddress",
        "@missingusername.com",
        "username@.com",
        "username@com",
        "username@domain..com",
        "username@domain.c",
        "username@-domain.com",
        "username@domain-.com",
    ]

    while True:
        user_email = input(Fore.CYAN + "Enter an email to test: ").strip()
        if validate_email(user_email):
            print(Fore.GREEN + f"Your Input '{user_email}': Valid")
        else:
            print(Fore.RED + f"Your Input '{user_email}': Invalid")

        print(Fore.YELLOW + "\n--- Running Edge-Case Tests for Email ---")
        for case in valid_email_cases:
            if validate_email(case):
                print(Fore.GREEN + f"Edge Case '{case}': Valid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Valid)")
        for case in invalid_email_cases:
            if not validate_email(case):
                print(Fore.RED + f"Edge Case '{case}': Invalid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Invalid)")
        print(Fore.YELLOW + "--- Finished Edge-Case Tests for Email ---\n")

        cont = input(Fore.LIGHTBLACK_EX + "Run another email test? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def run_phone_module():
    valid_phone_cases = [
        "+14155552671",
        "+250788123456"
    ]
    invalid_phone_cases = [
        "123",
        "0123456789",
        "++250788123456",
        "+250 788 123 456",
        "+250-788-123-456"
    ]

    while True:
        user_phone = input(Fore.CYAN + "Enter your phone number to test: ").strip()
        if validate_phone_number(user_phone):
            print(Fore.GREEN + f"Your Input '{user_phone}': Valid")
        else:
            print(Fore.RED + f"Your Input '{user_phone}': Invalid")

        print(Fore.YELLOW + "\n--- Running Edge-Case Tests for Phone ---")
        for case in valid_phone_cases:
            if validate_phone_number(case):
                print(Fore.GREEN + f"Edge Case '{case}': Valid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Valid)")
        for case in invalid_phone_cases:
            if not validate_phone_number(case):
                print(Fore.RED + f"Edge Case '{case}': Invalid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Invalid)")
        print(Fore.YELLOW + "--- Finished Edge-Case Tests for Phone ---\n")

        cont = input(Fore.LIGHTBLACK_EX + "Run another phone test? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def run_credit_module():
    valid_credit_cases = [
        "1234 5678 9012 3456",
        "1234-5678-9012-3456",
        "1234567890123456"
    ]
    invalid_credit_cases = [
        "1234_5678_9012_3456",
        "abcd efgh ijkl mnop"
    ]

    while True:
        user_credit = input(Fore.CYAN + "Enter your credit card number to test: ").strip()
        if validate_credit_card(user_credit):
            print(Fore.GREEN + f"Your Input '{user_credit}': Valid")
        else:
            print(Fore.RED + f"Your Input '{user_credit}': Invalid")

        print(Fore.YELLOW + "\n--- Running Edge-Case Tests for Credit Card ---")
        for case in valid_credit_cases:
            if validate_credit_card(case):
                print(Fore.GREEN + f"Edge Case '{case}': Valid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Valid)")
        for case in invalid_credit_cases:
            if not validate_credit_card(case):
                print(Fore.RED + f"Edge Case '{case}': Invalid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Invalid)")
        print(Fore.YELLOW + "--- Finished Edge-Case Tests for Credit Card ---\n")

        cont = input(Fore.LIGHTBLACK_EX + "Run another credit card test? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def run_time_module():
    valid_time_cases = [
        "14:30",
        "2:30 PM",
        "00:00",
        "12:59 AM"
    ]
    invalid_time_cases = [
        "24:00",
        "13:60",
        "0:00 PM",
        "25:00"
    ]

    while True:
        user_time = input(Fore.CYAN + "Enter time (12-hour / 24-hour): ").strip()
        if validate_time(user_time):
            print(Fore.GREEN + f"Your Input '{user_time}': Valid")
        else:
            print(Fore.RED + f"Your Input '{user_time}': Invalid")

        print(Fore.YELLOW + "\n--- Running Edge-Case Tests for Time ---")
        for case in valid_time_cases:
            if validate_time(case):
                print(Fore.GREEN + f"Edge Case '{case}': Valid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Valid)")
        for case in invalid_time_cases:
            if not validate_time(case):
                print(Fore.RED + f"Edge Case '{case}': Invalid")
            else:
                print(Fore.RED + f"Edge Case '{case}': Failed (should be Invalid)")
        print(Fore.YELLOW + "--- Finished Edge-Case Tests for Time ---\n")

        cont = input(Fore.LIGHTBLACK_EX + "Run another time test? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def main():
    while True:
        print(Fore.MAGENTA + "\nWelcome to the REGEX Onboarding Hackathon App!")
        print(Fore.MAGENTA + "Choose the type of validation you want to perform:")
        print(Fore.MAGENTA + "---------------------------------------------")
        print(Fore.BLUE + "Menu")
        print(Fore.MAGENTA + "---------------------------------------------")
        print(Fore.MAGENTA + "1. Email Validation")
        print(Fore.MAGENTA + "2. Phone Number Validation")
        print(Fore.MAGENTA + "3. Credit Card Validation")
        print(Fore.MAGENTA + "4. Time Validation (12-hour / 24-hour)")
        print(Fore.MAGENTA + "Q. Quit")
        choice = input(Fore.CYAN + "Enter your choice: ").strip().lower()

        if choice == '1':
            run_email_module()
        elif choice == '2':
            run_phone_module()
        elif choice == '3':
            run_credit_module()
        elif choice == '4':
            run_time_module()
        elif choice == 'q':
            print(Fore.CYAN + "Thank you for using the REGEX Onboarding Hackathon App. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
