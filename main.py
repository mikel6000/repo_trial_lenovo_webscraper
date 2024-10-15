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

username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Set chrome
chrome_options = Options()

# Basic options
chrome_options.add_argument('--incognito')
# chrome_options.add_argument("--headless=old")
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--verbose')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-software-rasterizer')

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
end_num = 9

# Define numbers to skip
skip_numbers_plus = {}

# Define the DataFrame with the specified headers
df = pd.DataFrame(columns=[
    'Case ID',
    'Case type',
    'Case name',
    'Version',
    'Keywords',
    'Auto type',
    'Workloading',
    'Priority',
    'Creator',
    'Category folder',
    'Execution Type',
    'Status',
    'OS',
    'Phase',
    'Owner',
    'Objective',
    'Release notes',
    'Type matrix',
    'Case tools',
    # 'Attachments',
])

# Loop through the specified range to expand/dropdown
for i in range(start_num, end_num + 1):
    element_id = f"webfx-tree-object-{i}-plus"

# element_id = [
#     f"webfx-tree-object-{i}-plus"
#     for i in range(start_num, end_num + 1) if i not in skip_numbers_plus
# ]

    try:
        icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element_id)))
        ActionChains(driver).move_to_element(icon).perform()
        icon.click()
        WebDriverWait(driver, 2) # Wait for the dropdown to expand

    except Exception as e:
        print(f"Could not click icon with ID {element_id}: {e}")
        continue

###### Version 1
# List of specific numbers to include in the xpaths
# numbers = [6, 7, 8, 9, 11, 14, 16, 17, 18, 19, 21]

# Generate the xpaths dynamically
# xpaths_of_anchor_folders = [f"webfx-tree-object-{num}-anchor" for num in numbers]
########## End of version 1

###### Version 2
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
end = 9 #this number is not included (ex.209 next run shoud be 210)

# Define numbers to skip
skip_numbers = {}

# Generate the xpaths dynamically, skipping unwanted numbers
xpaths_of_anchor_folders = [
    f"webfx-tree-object-{num}-anchor"
    for num in range(start, end) if num not in skip_numbers
]
######### End of version 2

# Loop through each anchor folder and click TC-xpath
for anchor_id in xpaths_of_anchor_folders:
    try:
        anchor_folder = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, anchor_id))
        )
        driver.execute_script("arguments[0].click();", anchor_folder)

        # Get the number of test case rows present
        row_elements = driver.find_elements(By.XPATH, '//*[@id="caseList"]/tbody/tr')
        num_rows = len(row_elements)

        print(f"Anchor folder '{anchor_id}' has {num_rows} test case(s).")

        # List of TC-XPaths based on the actual number of rows
        xpaths_of_test_cases = [
            f'//*[@id="caseList"]/tbody/tr[{i}]/td[1]/a' for i in range(1, num_rows + 1)
        ]

        # Create a temporary DataFrame to hold new rows
        temp_df = pd.DataFrame(columns=df.columns)

        # Loop through each test case XPath to click and retrieve data
        for test_case_xpath in xpaths_of_test_cases:
            try:
                test_case_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, test_case_xpath)))
                ActionChains(driver).move_to_element(test_case_element).perform()
                test_case_element.click()

                # Function to get data or return 'NULL'
                def get_value(xpath):
                    try:
                        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                        value = element.get_attribute('value') if element else 'NULL'
                        return value
                    except Exception:
                        print(f"Could not retrieve value from {xpath}: Returning 'NULL'")
                        return 'NULL'

                def get_text(xpath):
                    try:
                        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                        text = element.text.strip() if element else 'NULL'
                        return text
                    except Exception:
                        print(f"Could not retrieve text from {xpath}: Returning 'NULL'")
                        return 'NULL'
                    
                def get_option_values(select_xpath):
                    try:
                        select_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, select_xpath)))
                        # Find all option elements within the select element
                        option_elements = select_element.find_elements(By.TAG_NAME, "option")
                        # Retrieve the value of each option
                        #option_values = [option.get_attribute('value') for option in option_elements]
                        option_values = [option.text for option in option_elements]
                        return ', '.join(option_values) if option_values else 'NULL'
                    except Exception as e:
                        # print(f"Could not retrieve option values from {select_xpath}: {e}")
                        print(f"Could not retrieve option values from {select_xpath}")
                        return 'NULL'
                    
                # Collect data
                case_id = get_value('//*[@id="caseViewForm_caseBO_caseAlias"]')
                case_type = get_value('//*[@id="caseViewForm_caseBO_caseClassName"]')
                case_name = get_value('//*[@id="caseViewForm_caseBO_caseName"]')
                version = get_value('//*[@id="caseViewForm_caseBO_version"]')
                keywords = get_value('//*[@id="caseViewForm_caseBO_keyword"]')
                auto_type = get_value('//*[@id="selautoType"]')
                workloading = get_value('//*[@id="caseViewForm_caseBO_workloading"]')
                priority = get_value('//*[@id="caseViewForm_caseBO_priorityName"]')
                creator = get_value('//*[@id="caseViewForm_caseBO_creator"]')
                category_folder = get_value('//*[@id="caseViewForm_caseBO_categoryName"]')
                execution_type = get_value('//*[@id="caseViewForm_caseBO_caseType"]')
                status = get_value('//*[@id="caseViewForm_caseBO_isactive"]')
                os_value = get_option_values('//*[@id="caseViewForm_osList"]')
                phase = get_value('//*[@id="caseViewForm_caseBO_selectedTags"]')
                owner = get_value('//*[@id="caseViewForm_caseBO_owner"]')
                objective = get_text('//*[@id="objectiveDiv"]')
                release_notes = get_value('//*[@id="descriptionDiv"]')
                type_matrix = get_option_values('//*[@id="caseMatrix"]')
                case_tools = get_value('//*[@id="caseTool"]')

                # Create a dictionary to hold the data
                row_data = {
                    'Case ID': case_id,
                    'Case type': case_type,
                    'Case name': case_name,
                    'Version': version,
                    'Keywords': keywords,
                    'Auto type': auto_type,
                    'Workloading': workloading,
                    'Priority': priority,
                    'Creator': creator,
                    'Category folder': category_folder,
                    'Execution Type': execution_type,
                    'Status': status,
                    'OS': os_value,
                    'Phase': phase,
                    'Owner': owner,
                    'Objective': objective,
                    'Release notes': release_notes,
                    'Type matrix': type_matrix,
                    'Case tools': case_tools,
                }

                # Append the row data to the temporary DataFrame
                temp_df = pd.concat([temp_df, pd.DataFrame([row_data])], ignore_index=True)

                driver.back()

            except Exception as e:
                # print(f"Could not click the test case element with XPath {test_case_xpath}: {e}")
                print(f"Could not click the test case element with XPath {test_case_xpath}")
                continue

        # Concatenate the temporary DataFrame to the main DataFrame
        df = pd.concat([df, temp_df], ignore_index=True)
        # print(f"Processed anchor folder '{anchor_id}' with {num_rows} test case(s).")

    except Exception as e:
        # print(f"Could not click the anchor folder with XPath {anchor_id}: {e}")
        print(f"Could not click the anchor folder with XPath {anchor_id}")
        continue

end_time_scriptrun = time.time()

# Display or save the DataFrame
print(df)

# Save to a CSV file
file_path = 'TC_TDMS_data.csv'
#df.to_csv('output.csv', index=False)

# Check if the file already exists
if os.path.exists(file_path):
    # If the file exists, append without header
    df.to_csv(file_path, mode='a', index=False, header=False)
else:
    # If the file does not exist, create it with header
    df.to_csv(file_path, mode='w', index=False, header=True)

# Close the driver when done
time.sleep(5)
driver.quit()

# Calculate the elapsed time
elapsed_time_scriptrun = end_time_scriptrun - start_time_scriptrun
print("--------------------------------")
print(f"Code started at: {time.ctime(start_time_scriptrun)}")
print(f"Code ended at: {time.ctime(end_time_scriptrun)}")
print(f"Total elapsed time: {elapsed_time_scriptrun:.2f} seconds")