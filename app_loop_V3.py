#Version3 : Dynamic header, it retreive the header from the web
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
def navigate_and_collect_data(driver, folder_ids, xpaths):
    for folder_id in folder_ids:
        driver.find_element(By.ID, folder_id).click()

    # Final click to navigate into the folder
    driver.find_element(By.XPATH, xpaths['navigate']).click()

    # Retrieve case data headers and values
    headers = {
        'case_type': driver.find_element(By.XPATH, xpaths['case_type_text']).text,
        'case_id': driver.find_element(By.XPATH, xpaths['case_id_text']).text,
        'case_name': driver.find_element(By.XPATH, xpaths['case_name_text']).text
    }

    values = {
        'case_type': driver.find_element(By.XPATH, xpaths['case_type_field']).get_attribute("value"),
        'case_id': driver.find_element(By.XPATH, xpaths['case_id_field']).get_attribute("value"),
        'case_name': driver.find_element(By.XPATH, xpaths['case_name_field']).get_attribute("value")
    }

    return headers, values

# Save data to CSV file
# def save_to_csv(file_path, data):
#     with open(file_path, mode='w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(data.values())



'''Main Script'''
# output_folder = 'output_csv'
# create_output_folder(output_folder)
# csv_file_path = os.path.join(output_folder, 'output_data.csv')

# DataFrame to store all cases
df = pd.DataFrame(columns=['case_id', 'case_type', 'case_name'])

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

# Define folders and corresponding xpaths
folders = [
    {
        'ids': ['menu_system_test', 'webfx-tree-object-3-plus', 'webfx-tree-object-4-plus', 'webfx-tree-object-5-plus', 'webfx-tree-object-6-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            'case_type_text': '//*[@id="basicdiv"]/table/tbody/tr[1]/td[1]',
            'case_id_text': '//*[@id="basicdiv"]/table/tbody/tr[1]/td[5]',
            'case_name_text': '//*[@id="basicdiv"]/table/tbody/tr[2]/td[1]',
            'case_type_field': '//*[@id="caseViewForm_caseBO_caseClassName"]',
            'case_id_field': '//*[@id="caseViewForm_caseBO_caseAlias"]',
            'case_name_field': '//*[@id="caseViewForm_caseBO_caseName"]'
        }
    },
    {
        'ids': ['id2_a', 'id2_b', 'id2_c', 'id2_d', 'id2_e'],
        'xpaths': {
            'navigate': '//*xpath2',
            'case_type_text': '//*xpath_text2',
            'case_id_text': '//*xpath_text_id2',
            'case_name_text': '//*xpath_text_name2',
            'case_type_field': '//*xpath_value_type2',
            'case_id_field': '//*xpath_value_id2',
            'case_name_field': '//*xpath_value_name2'
        }
    },
    # Add additional folder definitions here
]

# Loop through each folder to collect data
for folder in folders:
    headers, values = navigate_and_collect_data(driver, folder['ids'], folder['xpaths'])
    
    # Create a DataFrame for the current data
    temp_df = pd.DataFrame([{
        headers['case_type']: values['case_type'],
        headers['case_id']: values['case_id'],
        headers['case_name']: values['case_name']
    }])
    
    # Concatenate the current data with the main DataFrame
    df = pd.concat([df, temp_df], ignore_index=True)

# Print the gathered data
print(df)

# Close the driver when done
# time.sleep(5)
driver.quit()
print("Process Complete")