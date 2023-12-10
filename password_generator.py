import random
import string


## two params - number and special_characters - are needed to pass to function to call it
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    ## starting a loop, every new iteration generates new characters to add to random password until criteria is met
    # setting up variables
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # chain conditional with 'and' keyword
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


## asking the user to give us this information
min_length = int(
    input("Enter the minimum lenght: ")
)  # convert to integer b/c we need a number value
has_number = (
    input("Do you want to have numbers (y/n)? ").lower() == "y"
)  # converts to lowercase and a boolean
has_special = (
    input("Do you want to have special characters (y/n)? ").lower() == "y"
)  # converts to lowercase and a boolean

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
