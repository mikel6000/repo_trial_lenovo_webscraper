#Semi official

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

username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Set chrome
chrome_options = Options()

# Basic options
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
#driver.find_element(By.ID, 'menu_system_test').click() # Navigate to the Test case DB
WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, 'menu_system_test'))
).click()

# Specify the range of numbers for your IDs
start_num = 3
end_num = 10

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

    try:
        icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element_id)))
        ActionChains(driver).move_to_element(icon).perform()
        icon.click()
        WebDriverWait(driver, 2) # Wait for the dropdown to expand

    except Exception as e:
        print(f"Could not click icon with ID {element_id}: {e}")
        continue

# List of XPaths to click (anchor folder)
xpaths_of_anchor_folders = [
    "webfx-tree-object-6-anchor",
    "webfx-tree-object-7-anchor",
    "webfx-tree-object-8-anchor",
    "webfx-tree-object-9-anchor",
]

# Loop through each anchor folder and click TC-xpath
for anchor_id in xpaths_of_anchor_folders:
    try:
        # anchor_folder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, anchor_xpath)))
        anchor_folder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,anchor_id)))
        ActionChains(driver).move_to_element(anchor_folder).perform()
        anchor_folder.click()

        # List of TC-XPaths within the clicked anchor folder
        xpaths_of_test_cases = [
            '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
            '//*[@id="caseList"]/tbody/tr[3]/td[1]/a',
            # Add more XPaths as necessary
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
                # def get_value(xpath):
                #     try:
                #         return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).get_attribute('value')
                #     except Exception:
                #         return 'NULL'
                    
                def get_value(xpath):
                    try:
                        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                        value = element.get_attribute('value') if element else 'NULL'
                        #print(f"Retrieved value from {xpath}: '{value}'")
                        return value
                    except Exception:
                        print(f"Could not retrieve value from {xpath}: Returning 'NULL'")
                        return 'NULL'

                def get_text(xpath):
                    try:
                        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                        text = element.text.strip() if element else 'NULL'
                        #print(f"Retrieved text from {xpath}: '{text}'")
                        return text
                    except Exception:
                        print(f"Could not retrieve text from {xpath}: Returning 'NULL'")
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
                os_value = get_value('//*[@id="caseViewForm_osList"]')
                phase = get_value('//*[@id="caseViewForm_caseBO_selectedTags"]')
                owner = get_value('//*[@id="caseViewForm_caseBO_owner"]')
                objective = get_value('//*[@id="objectiveDiv"]')
                release_notes = get_value('//*[@id="descriptionDiv"]')
                type_matrix = get_text('//*[@id="caseMatrix"]')
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
                print(f"Could not click the test case element with XPath {test_case_xpath}: {e}")
                continue

        # Concatenate the temporary DataFrame to the main DataFrame
        df = pd.concat([df, temp_df], ignore_index=True)

    except Exception as e:
        print(f"Could not click the anchor folder with XPath {anchor_id}: {e}")
        continue

# Display or save the DataFrame
print(df)
# Save to a CSV file
df.to_csv('output.csv', index=False)

# Close the driver when done
time.sleep(5)
driver.quit()