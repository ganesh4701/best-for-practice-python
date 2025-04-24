# generate passwords
# length of password
# should contains uppercase, lowercase, digits and symbols
# ask user for length of password
# ask user for number of passwords to generate
# generate passwords

import random
import string

def generate_password():
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower()
    include_digits = input("Include digits? (y/n): ").strip().lower()
    include_symbols = input("Include symbols? (y/n): ").strip().lower()

    if length < 4:
        print("Password length should be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase if include_lowercase == 'y' else ''
    upper = string.ascii_uppercase if include_uppercase == 'y' else ''
    digits = string.digits if include_digits == 'y' else ''
    symbols = string.punctuation if include_symbols == 'y' else ''

    all_characters = lower + upper + digits + symbols

    required_characaters = []
    if include_uppercase == 'y':
        required_characaters.append(random.choice(upper))
    if include_lowercase == 'y':
        required_characaters.append(random.choice(lower))
    if include_digits == 'y':
        required_characaters.append(random.choice(digits))
    if include_symbols == 'y':
        required_characaters.append(random.choice(symbols))

    remaining_length = length - len(required_characaters)
    password = required_characaters

    for i in range(remaining_length):
        password.append((random.choice(all_characters)))
    random.shuffle(password)

    str_password = "".join(password)

    return f'Generated password: {str_password}'

print(generate_password())
