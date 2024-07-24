import random
import string

def generate_pass(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits    
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character type used or selected. Try again."
    
    passkey = ""
    for _ in range(length):
        passkey += random.choice(characters)
    return passkey

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password you want to enter: "))
    use_letters = input("Want to include letters (y/n)? ") .lower() == 'y'
    use_numbers = input("Want to include numbers (y/n)? ") .lower() == 'y'
    use_symbols = input("Want to include symbols (y/n)? ") .lower() == 'y'

    passkey = generate_pass(length, use_letters, use_numbers, use_symbols)

    print("Generated Password is:", passkey)
if __name__ == "__main__":
    main()
    