# Script to login and navigate
# Note: before running this file you need to create variables in the os for the login credentials

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Set chrome
chrome_options = Options()

# Basic options
# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument('--incognito')


# Initialize the WebDriver
driver_path = 'C:/Users/michaeljohn.roguel/Documents/GitHub/repo_trial_lenovo_webscraper/chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')


# Use the credentials to log in
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'loginsub').click()
driver.refresh()

#Navigate to the Test case DB
driver.find_element(By.ID, 'menu_system_test').click()
driver.find_element(By.ID, 'webfx-tree-object-3-plus').click() #ThinkPad SW Test Case '+' sign

# Expand to Android
def expand_to_android():
    driver.find_element(By.ID, 'webfx-tree-object-4-plus').click()
    driver.find_element(By.ID, 'webfx-tree-object-5-plus').click() #Android
    #driver.find_element(By.ID, 'webfx-tree-object-6-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-10-plus').click() #FFRT for Android
    #driver.find_element(By.ID, 'webfx-tree-object-11-anchor').click() #Anchor folder
    

def expand_to_application():
    driver.find_element(By.ID, 'webfx-tree-object-12-plus').click()
    driver.find_element(By.ID, 'webfx-tree-object-13-plus').click() #AOAC
    #driver.find_element(By.ID, 'webfx-tree-object-14-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-15-plus').click() #Application
    #driver.find_element(By.ID, 'webfx-tree-object-16-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-17-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-18-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-19-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-20-plus').click() #Auto Screen Rotation Util
    #driver.find_element(By.ID, 'webfx-tree-object-21-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-22-plus').click() #Battery
    #driver.find_element(By.ID, 'webfx-tree-object-23-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-24-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-25-plus').click() #Computrace
    #driver.find_element(By.ID, 'webfx-tree-object-26-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-27-plus').click() #Digitizer
    #driver.find_element(By.ID, 'webfx-tree-object-28-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-29-plus').click() #Dual Mode Battery
    #driver.find_element(By.ID, 'webfx-tree-object-30-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-31-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-32-plus').click() #DVD
    #driver.find_element(By.ID, 'webfx-tree-object-33-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-34-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-35-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-36-plus').click() #FFRT
    #driver.find_element(By.ID, 'webfx-tree-object-37-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-38-plus').click() #Finger Print Reader
    #driver.find_element(By.ID, 'webfx-tree-object-39-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-40-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-41-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-42-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-43-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-44-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-45-plus').click() #Google Chrome OS
    #driver.find_element(By.ID, 'webfx-tree-object-46-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-47-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-48-plus').click() #HDD Active Protection Sys
    #driver.find_element(By.ID, 'webfx-tree-object-49-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-50-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-51-anchor').click() #Anchor folder
    driver.find_element(By.ID, 'webfx-tree-object-52-plus').click() #Hotkey
    #driver.find_element(By.ID, 'webfx-tree-object-53-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-54-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-55-anchor').click() #Anchor folder
    #driver.find_element(By.ID, 'webfx-tree-object-56-anchor').click() #Anchor folder





expand_to_android()
expand_to_application()

# Close the driver when done
time.sleep(3)
driver.quit()
# print("Process Complete")