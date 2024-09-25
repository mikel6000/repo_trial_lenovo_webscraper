from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read the encrypted credentials
with open('encrypted_credentials.txt', 'rb') as file:
    encrypted = file.read()

# Decrypt the credentials
decrypted = cipher.decrypt(encrypted).decode()

# Parse the credentials
credentials = dict(line.split('=') for line in decrypted.splitlines())

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')

# Use the credentials to log in
username = driver.find_element(By.ID, 'username')
username.send_keys(credentials['username'])
password = driver.find_element(By.ID, 'password')
password.send_keys(credentials['password'])
driver.find_element(By.ID, 'loginsub').click()

# Close the driver when done
time.sleep(3)
driver.quit()
print("Process Complete")

# Find the username and password fields and enter credentials
# username_field = driver.find_element(By.ID, 'MainContent_textUserID')
# password_field = driver.find_element(By.ID, 'MainContent_textPassword')
# username_field.send_keys(username)
# password_field.send_keys(password)