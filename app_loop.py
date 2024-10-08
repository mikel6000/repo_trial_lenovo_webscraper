#note: before running this file you need to create variables in the os for the login credentials

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

# Create folder for the CSV output
def create_output_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Navigate and retrieve data
def navigate_and_get_data(driver, folder_ids, xpath_click, xpaths):
    for folder_id in folder_ids:
        driver.find_element(By.ID, folder_id).click()
    
    driver.find_element(By.XPATH, xpath_click).click()

    case_data = {
        'case_type': driver.find_element(By.XPATH, xpaths['case_type']).text,
        'case_type_field': driver.find_element(By.XPATH, xpaths['case_type_field']).get_attribute("value"),
        'case_id': driver.find_element(By.XPATH, xpaths['case_id']).text,
        'case_id_field': driver.find_element(By.XPATH, xpaths['case_id_field']).get_attribute("value"),
        'case_name': driver.find_element(By.XPATH, xpaths['case_name']).text,
        'case_name_field': driver.find_element(By.XPATH, xpaths['case_name_field']).get_attribute("value"),
    }
    
    return case_data

# Save data to CSV file
# def save_to_csv(file_path, data):
#     with open(file_path, mode='w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(data.values())



'''Main Script'''
output_folder = 'output_csv'
create_output_folder(output_folder)
csv_file_path = os.path.join(output_folder, 'output_data.csv')

# Access credentials from environment variables
username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Set chrome
# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()

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

# First folder navigation and data retrieval
folder_ids_1 = ['menu_system_test', 'webfx-tree-object-3-plus', 'webfx-tree-object-4-plus', 'webfx-tree-object-5-plus', 'webfx-tree-object-6-anchor']
xpaths_1 = {
    'case_type': '//*[@id="basicdiv"]/table/tbody/tr[1]/td[1]',
    'case_type_field': '//*[@id="caseViewForm_caseBO_caseClassName"]',
    'case_id': '//*[@id="basicdiv"]/table/tbody/tr[1]/td[5]',
    'case_id_field': '//*[@id="caseViewForm_caseBO_caseAlias"]',
    'case_name': '//*[@id="basicdiv"]/table/tbody/tr[2]/td[1]',
    'case_name_field': '//*[@id="caseViewForm_caseBO_caseName"]'
}
case_data_1 = navigate_and_get_data(driver, folder_ids_1, '//*[@id="caseList"]/tbody/tr[1]/td[1]/a', xpaths_1)
print(case_data_1)
# save_to_csv(csv_file_path, case_data_1)

# Close the driver when done
# time.sleep(5)
driver.quit()
print("Process Complete")