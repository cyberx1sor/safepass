# safepass - Secure Password Generator Documentation

## Introduction
The Secure Password Generator is a Python program that generates strong and secure passwords based on user-defined criteria. It ensures that the generated passwords meet specific requirements for length, uppercase letters, lowercase letters, digits, and symbols. The program allows users to input the desired length of the password and generates a random password that satisfies the given criteria.

## Usage
1. Ensure that Python is installed on your system.
2. Run the program using a Python interpreter.
3. Follow the on-screen prompts to input the desired length of the password.
4. The program will generate a random password that satisfies the given criteria and display it on the screen.

## Requirements
- Python 3.x

## Functionality
1. User Input:
   - The program prompts the user to enter the desired length for the password.
   - If the user enters a length less than 8, an error message is displayed, and the user is prompted again until a valid length is provided.

2. Password Generation:
   - The program generates a random password that satisfies the following criteria:
     - Length: The password length is equal to or greater than the user-defined length (with a minimum of 8 characters).
     - Uppercase Letters: The password contains at least 2 uppercase letters.
     - Lowercase Letters: The password contains at least 2 lowercase letters.
     - Digits: The password contains at least 2 digits.
     - Symbols: The password contains at least one symbol (punctuation character).

3. Password Display:
   - The generated password is displayed on the screen for the user to see and utilize.

## Example Usage
```
python safepass.py
```

Enter the desired length for the password: 12

Generated password: X5t$1hA7&z9Z

## Notes
- The program relies on the random and string modules in Python for password generation.
- It enforces a minimum password length of 8 characters, even if the user enters a shorter length.
- Users are encouraged to store generated passwords securely and avoid reusing them across different accounts.
