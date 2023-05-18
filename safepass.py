import random
import string

def generate_password(length):
    min_length = max(length, 8)
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(min_length))
        # Verify that the password meets the requirements
        if (
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c.islower() for c in password) and
            any(c in string.punctuation for c in password) and
            sum(c.isupper() for c in password) >= 2 and
            sum(c.isdigit() for c in password) >= 2 and
            sum(c.islower() for c in password) >= 2
        ):
            return password

if __name__ == "__main__":
    while True:
        password_length = int(input("Enter the desired length for the password: "))
        if password_length < 12:
            print("The minimum password length is 12 characters. Please try again.")
        else:
            break

    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")
