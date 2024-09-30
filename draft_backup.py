from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Access credentials directly from environment variables
username = os.getenv('ci_username')
password = os.getenv('ci_password')

# Debugging: Print credentials
# print(f"Username: {username}")
# print(f"Password: {password}")

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://thewebsite.com')

# Use the credentials to log in
username_textbox = driver.find_element(By.ID, 'username').send_keys(f'{username}')
password_textbox = driver.find_element(By.ID, 'password').send_keys(f'{password}')
# driver.find_element(By.ID, 'loginsub').click()

# Close the driver when done
time.sleep(3)
driver.quit()
print("Process Complete")