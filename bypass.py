#Static Header, acts like a template. Only retrieves data from the 'field' element
#note: before running this file you need to create variables in the os for the login credentials

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

# Navigate and retrieve data
def navigate_and_collect_data(driver, folder_ids, xpaths):
    for folder_id in folder_ids:
        # driver.find_element(By.ID, folder_id).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, folder_id))
    ).click()

    # Final click to navigate into the folder
    # driver.find_element(By.XPATH, xpaths['navigate']).click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpaths['navigate']))
    ).click()

    # Locate the tbody element
    # tbody = driver.find_element(By.TAG_NAME, 'tbody')
    tbody = driver.find_element(By.TAG_NAME, 'form')

    # Get all rows in the tbody
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    # Loop through each row and get the cell data
    for row in rows:
        # Get all cells (td) in the current row
        cells = row.find_elements(By.TAG_NAME, 'td')
        cell_data = [cell.text for cell in cells]  # Extract text from each cell
        print(cell_data)


# Access credentials from environment variables
username = os.getenv('zlen_username')
password = os.getenv('zlen_password')


# Initialize Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("disable-images")

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')

# Use the credentials to log in
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'loginsub').click()
driver.refresh()

# Define folders and corresponding xpaths
folders = [
    {
        #TC-4576PA
        'ids': ['menu_system_test', 'webfx-tree-object-3-plus', 'webfx-tree-object-4-plus', 'webfx-tree-object-5-plus', 'webfx-tree-object-6-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
       }
    }
]

for folder in folders:
    data = navigate_and_collect_data(driver, folder['ids'], folder['xpaths'])

# Close the driver when done
driver.quit()
print("Process Complete")