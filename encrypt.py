### note: before running this script make sure you already added the environment variable:
# set MY_APP_USERNAME=your_username
# set MY_APP_PASSWORD=your_password

import os
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the key
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Get credentials from environment variables
username = os.getenv('z_username')
password = os.getenv('z_password')

# Check if credentials are set in the OS
# if not username or not password:
#     raise ValueError("Environment variables for username or password are not set.")

# Encrypt the credentials
credentials = f"username={username}\npassword={password}".encode()
encrypted = cipher.encrypt(credentials)

# Save the encrypted data to a file
with open('encrypted_credentials.txt', 'wb') as file:
    file.write(encrypted)
    
# print(f"Username: {username}")
# print(f"Password: {password}")

print("Credentials encrypted and saved.")