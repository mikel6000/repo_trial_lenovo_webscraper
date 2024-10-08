#note: before running this file you need to create variables in the os for the login credentials

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

# Navigate to 1st Folder
driver.find_element(By.ID, 'menu_system_test').click()
driver.find_element(By.ID, 'webfx-tree-object-3-plus').click()
driver.find_element(By.ID, 'webfx-tree-object-4-plus').click()
driver.find_element(By.ID, 'webfx-tree-object-5-plus').click()
driver.find_element(By.ID, 'webfx-tree-object-6-anchor').click()
driver.find_element(By.XPATH, '//*[@id="caseList"]/tbody/tr[1]/td[1]/a').click()

# Create folder for the CSV output
# Your code here

# Navigate to 1st Folder
driver.find_element(By.ID, 'id1').click()
driver.find_element(By.ID, 'id2').click()
driver.find_element(By.ID, 'id3').click()
driver.find_element(By.ID, 'id4').click()
driver.find_element(By.ID, 'id5').click()
driver.find_element(By.XPATH, '//*xpath').click()

# Get the data
case_type = driver.find_element(By.XPATH, '//*xpath').text
case_type_field = driver.find_element(By.XPATH, '//*xpath').get_attribute("value")

case_id = driver.find_element(By.XPATH, '//*xpath').text
case_id_field = driver.find_element(By.XPATH, '//*xpath').get_attribute("value")

case_name = driver.find_element(By.XPATH, '//*xpath').text
case_name_field = driver.find_element(By.XPATH, '//*xpath').get_attribute("value")

# Save Output to CSV file
# Your code here

# Navigate to 2nd Folder
driver.find_element(By.ID, 'id1').click()
driver.find_element(By.ID, 'id2').click()
driver.find_element(By.ID, 'id3').click()
driver.find_element(By.ID, 'id4').click()
driver.find_element(By.ID, 'id5').click()
driver.find_element(By.XPATH, '//*xpath').click()

# Get the data
case_type = driver.find_element(By.XPATH, '//*xpath').text
case_type_field = driver.find_element(By.XPATH, '//*xpath').get_attribute("value")

case_id = driver.find_element(By.XPATH, '//*xpath').text
case_id_field = driver.find_element(By.XPATH, '//*xpath').get_attribute("value")

case_name = driver.find_element(By.XPATH, '//*xpath').text
case_name_field = driver.find_element(By.XPATH, '//*xpath').get_attribute("value")

# Save Output to CSV file
# Your code here


# category_folder = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[2]/td[5]').text
# category_folder_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_categoryName"]').get_attribute("value")
# print(f'{category_folder} {category_folder_field}')

# version = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[3]/td[1]').text
# version_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_version"]').get_attribute("value")
# print(f'{version} {version_field}')

# execution_type = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[3]/td[5]').text
# execution_type_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_caseType"]').get_attribute("value")
# print(f'{execution_type} {execution_type_field}')

# Close the driver when done
time.sleep(5)
driver.quit()
print("Process Complete")