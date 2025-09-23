REGEX Onboarding Hackathon App

Welcome to the REGEX Onboarding Hackathon App! 
This is a simple and interactive command-line application that allows you to validate emails, phone numbers, credit card numbers, and time formats using regular expressions (regex).

The app also includes edge-case testing for each module individually, so you can see which inputs are valid or invalid, making it perfect for learning and testing regex patterns.

Features

✅ Email Validation – Checks if an email is properly formatted.

✅ Phone Number Validation – Validates international phone numbers using the E.164 standard.

✅ Credit Card Validation – Checks for standard card formats (Visa, MasterCard, Amex).

✅ Time Validation – Supports both 12-hour and 24-hour formats.

🟡 Edge-Case Tests – Runs predefined examples for each module to show valid and invalid cases.

🔄 Repeat Tests – Test multiple inputs without restarting the app.

🌈 Color-Coded Output –

Green: Valid input

Red: Invalid input

Yellow: Running edge-case tests

Installation

Clone the repository:

git clone https://github.com/your-username/alu_regex-data-extraction-Airman-web.git


Navigate to the project folder:

cd alu_regex-data-extraction-Airman-web


Install dependencies (if not already installed):

pip3 install colorama

How to Use

Run the app:

python3 Main_App.py


Interactive Menu:

Welcome to the REGEX Onboarding Hackathon App!
---------------------------------------------
Menu
---------------------------------------------
1. Email Validation
2. Phone Number Validation
3. Credit Card Validation
4. Time Validation (12-hour / 24-hour)
Q. Quit
Enter your choice:


Choose an option by typing the number:

1 – Email

2 – Phone Number

3 – Credit Card

4 – Time

Q – Quit the app

Follow the prompts to enter your input. The app will instantly tell you whether it’s valid or invalid.

Repeat testing as many times as needed without returning to the main menu.

Edge-Case Testing

When you run each module:

The app will highlight each edge case in yellow.

Valid inputs appear in green, and invalid inputs appear in red.

Each module (Email, Phone, Credit Card, Time) can be tested individually, immediately after your input.

This helps you understand which patterns work and see common mistakes.

Example Output

Email Validation Example:

Enter an email to test: e.atigbi@alustudent.com
Your Input 'e.atigbi@alustudent.com': Valid

--- Running Edge-Case Tests for Email ---
Edge Case 'test@example.com': Valid
Edge Case 'user.name@domain.co': Valid
Edge Case 'plainaddress': Invalid
Edge Case '@missingusername.com': Invalid
Edge Case 'username@.com': Invalid
--- Finished Edge-Case Tests for Email ---


Color Legend:

✅ Green → Valid

❌ Red → Invalid

🟡 Yellow → Edge-case testing

Contributing

Feel free to fork this repository, improve regex patterns, or add more edge-case examples.

License

This project is open source and available under the MIT License.
