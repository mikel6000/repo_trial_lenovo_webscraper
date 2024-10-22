# Script for collecting data on TDMS website
# Note: before running this file you need to create variables in the os for the login credentials

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd

start_time_scriptrun = time.time()
case_library_dir = "C:/Users/Development 2/Documents/LENOVO/TEST_PLAN_AI/Case library"
os.makedirs(case_library_dir, exist_ok=True)

username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Set chrome
chrome_options = Options()

# Basic options
chrome_options.add_argument('--incognito')
# chrome_options.add_argument("--headless=old")

# Initialize the WebDriver
driver_path = 'C:/Users/Development 2/Documents/GitHub/repo_trial_lenovo_webscraper/chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')

# Use the credentials to log in
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'loginsub').click()
driver.refresh()
WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, 'menu_system_test'))
).click()

# Specify the range number for the PlusIcons
"""
(1) for Android and Applications (3-209)
(2) for Bios and Common (?-360)
(3) for Mobile and MS Logo (?-452)
(4) for Multimedia and Network (?-617)
(5) for Option and Preload (?-678)
(6) for Scenario, UX, and 00_Tools (?-702)
"""
start_num = 3
end_num = 109

# Define numbers to skip
skip_numbers_plus = {}

# Loop through the specified range to expand/dropdown
for i in range(start_num, end_num + 1):
    element_id = f"webfx-tree-object-{i}-plus"

    try:
        icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element_id)))
        ActionChains(driver).move_to_element(icon).perform()
        icon.click()
        WebDriverWait(driver, 2) # Wait for the dropdown to expand

    except Exception as e:
        print(f"Could not click icon with ID {element_id}: {e}")
        continue

# Specify the range number for the AnchorFolder
"""
(1) for Android and Applications (3-209)
(2) for Bios and Common (210-360)
(3) for Mobile and MS Logo (361-452)
(4) for Multimedia and Network (453-617)
(5) for Option and Preload (618-678)
(6) for Scenario, UX, and 00_Tools (679-702)
"""
start = 3 #plus 1 of the previous run
end = 109 #this number is not included (ex.209 next run shoud be 210)

# Define numbers to skip
skip_numbers = {}

# Generate the xpaths dynamically, skipping unwanted numbers
xpaths_of_anchor_folders = [
    f"webfx-tree-object-{num}-anchor"
    for num in range(start, end) if num not in skip_numbers
]

# Loop through each anchor folder and click TC-xpath
for anchor_id in xpaths_of_anchor_folders:
    try:
        anchor_folder = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, anchor_id)))
        click_anchor = driver.execute_script("arguments[0].click();", anchor_folder)

        # Get the number of test case rows present
        row_elements = driver.find_elements(By.XPATH, '//*[@id="caseList"]/tbody/tr')
        num_rows = len(row_elements)
        print(f"Anchor folder '{anchor_id}' has {num_rows} test case(s).")

        # List of TC-XPaths based on the actual number of rows
        xpaths_of_test_cases = [
            f'//*[@id="caseList"]/tbody/tr[{i}]/td[1]/a' for i in range(1, num_rows + 1)
        ]

        # Loop through each test case XPath to click and retrieve data
        for test_case_xpath in xpaths_of_test_cases:
            try:
                test_case_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, test_case_xpath)))
                ActionChains(driver).move_to_element(test_case_element).perform()
                test_case_element.click()
                case_id = driver.find_element(By.ID, 'caseViewForm_caseBO_caseAlias').get_attribute('value')
                print(case_id)
                tc_folder_path = os.path.join(case_library_dir, case_id)
                os.makedirs(tc_folder_path, exist_ok=True)

                driver.back()

            except Exception as e:
                print(f"Folder not created")
                continue

    except Exception as e:
        print(f"Could not click the anchor folder with XPath {anchor_id}")
        continue

end_time_scriptrun = time.time()

# Close the driver when done
time.sleep(5)
driver.quit()

# Calculate the elapsed time
elapsed_time_scriptrun = end_time_scriptrun - start_time_scriptrun
print("--------------------------------")
print(f"Code started at: {time.ctime(start_time_scriptrun)}")
print(f"Code ended at: {time.ctime(end_time_scriptrun)}")
print(f"Total elapsed time: {elapsed_time_scriptrun:.2f} seconds")