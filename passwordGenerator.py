import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define character sets for different types of characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    # Ensure each character type is included in the password
    password = [random.choice(uppercase_letters),
                random.choice(lowercase_letters),
                random.choice(digits),
                random.choice(symbols)]

    # Generate remaining characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

def generate_random_passwords(num_passwords, length=12):
    """Generate multiple random passwords."""
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))
    passwords = generate_random_passwords(num_passwords, length)
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)
