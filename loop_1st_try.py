#note: before running this file you need to create variables in the os for the login credentials

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

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

# Create folder for the CSV output
# Create a folder for CSV output
def create_output_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to navigate and retrieve data
def navigate_and_retrieve(driver, folder_ids, final_xpath, xpaths):
    # Navigate through each folder
    for folder_id in folder_ids:
        driver.find_element(By.ID, folder_id).click()

    driver.find_element(By.XPATH, final_xpath).click()
    
    # Retrieve data using the provided XPaths
    data = {}
    for key, xpath in xpaths.items():
        data[key] = driver.find_element(By.XPATH, xpath).text
        data[f"{key}_field"] = driver.find_element(By.XPATH, xpath).get_attribute("value")
    
    return data

def save_to_csv(data, filename):
    filepath = os.path.join(output_folder, filename)
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())



# Data for the first folder
folder1_ids = ['menu_system_test', 'webfx-tree-object-3-plus', 'webfx-tree-object-4-plus', 'webfx-tree-object-5-plus', 'webfx-tree-object-6-anchor']
folder1_final_xpath = '//*[@id="caseList"]/tbody/tr[1]/td[1]/a'
folder1_xpaths = {
    'case_type': '//*[@id="basicdiv"]/table/tbody/tr[1]/td[1]',
    'case_id': '//*xpath2',
    'case_name': '//*xpath3'
}
# Navigate to the first folder and retrieve data
data1 = navigate_and_retrieve(driver, folder1_ids, folder1_xpaths)
save_to_csv(data1, 'data_output.csv')

# Data for the second folder
folder2_ids = ['id1_2', 'id2_2', 'id3_2', 'id4_2', 'id5_2']
folder2_xpaths = {
    'case_type': '//*xpath4',
    'case_id': '//*xpath5',
    'case_name': '//*xpath6'
}

# Navigate to the second folder and retrieve data
data2 = navigate_and_retrieve(driver, folder2_ids, folder2_xpaths)
save_to_csv(data2, 'data_output.csv')

# Close the driver when done
time.sleep(5)
driver.quit()
print("Process Complete")