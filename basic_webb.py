from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os


# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.google.com/')

# Close the driver when done
time.sleep(3)
driver.quit()
print("Process Complete")