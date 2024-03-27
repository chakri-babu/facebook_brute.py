import requests

def check_credentials(username_or_email, password):
    # Construct the login URL
    login_url = 'https://www.facebook.com/login.php'

    # Create session
    session = requests.Session()

    # Send POST request with login data
    response = session.post(login_url, data={'email': username_or_email, 'pass': password})

    # Check if login was successful
    if 'Find Friends' in response.text:
        return True
    else:
        return False

# Main function
def main():
    # Input username/email and password
    username_or_email = input("Enter username or email: ")
    password1 = input("Enter first password to test: ")
    password2 = input("Enter second password to test: ")
    password3 = input("Enter third password to test: ")

    # Check each password
    passwords_to_check = [password1, password2, password3]
    for password in passwords_to_check:
        if check_credentials(username_or_email, password):
            print(f"Password match found: {password}")
            break
    else:
        print("None of the provided passwords match.")

if __name__ == "__main__":
    main()
