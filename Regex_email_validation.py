# Email vaildation using regex
import re
def validate_email(email):
    # Define the regex pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   
    # Use re.fullmatch to check if the email matches the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False





