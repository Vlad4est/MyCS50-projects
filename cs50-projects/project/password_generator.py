import random
import string


def generate_password(min_lenght, include_numbers=True, special_characters=True):
    characters = string.ascii_letters
    digits = 2 * string.digits
    special = string.punctuation


    if include_numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    check_conditions = False
    has_number = False
    has_special = False

    while not check_conditions or len(password) < min_lenght:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        check_conditions = True

        if include_numbers:
            check_conditions = has_number
        if special_characters:
            check_conditions = check_conditions and has_special

    return password