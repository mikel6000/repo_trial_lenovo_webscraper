import os
from cryptography.fernet import Fernet

# Check if the key file exists
if os.path.exists('secret.key'):
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
else:
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

cipher = Fernet(key)

# Get credentials from environment variables
username = os.getenv('MY_APP_USERNAME')
password = os.getenv('MY_APP_PASSWORD')

if not username or not password:
    raise ValueError("Environment variables for username or password are not set.")

# Encrypt the credentials
credentials = f"username={username}\npassword={password}".encode()

# Encrypt or update the existing encrypted file
encrypted = cipher.encrypt(credentials)
with open('encrypted_credentials.txt', 'wb') as file:
    file.write(encrypted)

print("Credentials encrypted and saved.")
