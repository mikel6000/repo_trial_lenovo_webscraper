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

# Create folder for the CSV output
# def create_output_folder(folder_name):
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)

# Navigate and retrieve data
def navigate_and_collect_data(driver, folder_ids, xpaths):
    driver.implicitly_wait(5)
    for folder_id in folder_ids:
        driver.find_element(By.ID, folder_id).click()
        # WebDriverWait(driver, 15).until(
        # EC.element_to_be_clickable((By.ID, folder_id))
        # ).click()

    # Click anchor to navigate into the folder
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, xpaths['navigate']).click()
    # WebDriverWait(driver, 15).until(
    # EC.element_to_be_clickable((By.XPATH, xpaths['navigate']))
    # ).click()

    # Retrieve case data
    case_data = {
        'Case ID': driver.find_element(By.XPATH, xpaths['case_id_field']).get_attribute("value"),
        'Case type': driver.find_element(By.XPATH, xpaths['case_type_field']).get_attribute("value"),
        'Case name': driver.find_element(By.XPATH, xpaths['case_name_field']).get_attribute("value"),
        'Version': driver.find_element(By.XPATH, xpaths['version_field']).get_attribute("value"),
        'Keywords': driver.find_element(By.XPATH, xpaths['keywords_field']).get_attribute("value"),
        'Auto type': driver.find_element(By.XPATH, xpaths['auto_type_field']).get_attribute("value"),
        'Workloading': driver.find_element(By.XPATH, xpaths['workloading_field']).get_attribute("value"),
        'Priority': driver.find_element(By.XPATH, xpaths['priority_field']).get_attribute("value"),
        'Creator': driver.find_element(By.XPATH, xpaths['creator_field']).get_attribute("value"),
        'Category folder': driver.find_element(By.XPATH, xpaths['category_folder_field']).get_attribute("value"),
        'Execution type': driver.find_element(By.XPATH, xpaths['execution_type_field']).get_attribute("value"),
        'Status': driver.find_element(By.XPATH, xpaths['status_field']).get_attribute("value"),
        'OS': driver.find_element(By.XPATH, xpaths['os_field']).get_attribute("value"),
        'Phase': driver.find_element(By.XPATH, xpaths['phase_field']).get_attribute("value"),
        'Owner': driver.find_element(By.XPATH, xpaths['owner_field']).get_attribute("value"),
        'Objective': driver.find_element(By.XPATH, xpaths['objective_field']).get_attribute("value"),
        'Release notes': driver.find_element(By.XPATH, xpaths['release_notes_field']).get_attribute("value"),
        #'Type matrix': driver.find_element(By.XPATH, xpaths['type_matrix_field']).get_attribute("value"),
        'Case tools': driver.find_element(By.XPATH, xpaths['case_tools_field']).get_attribute("value"),
        #'Attachments': driver.find_element(By.XPATH, xpaths['attachments_field']).text(),
    }

    driver.back()
    driver.implicitly_wait(10)
    
    return case_data


'''Main Script'''

# DataFrame to store all cases
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
#'Type matrix',
'Case tools',
#'Attachments',
])

# Access credentials from environment variables
username = os.getenv('zlen_username')
password = os.getenv('zlen_password')


# Initialize Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("disable-images")
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

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
common_xpaths = {
    'case_id_field': '//*[@id="caseViewForm_caseBO_caseAlias"]',
    'case_type_field': '//*[@id="caseViewForm_caseBO_caseClassName"]',
    'case_name_field': '//*[@id="caseViewForm_caseBO_caseName"]',
    'version_field': '//*[@id="caseViewForm_caseBO_version"]',
    'keywords_field': '//*[@id="caseViewForm_caseBO_keyword"]',
    'auto_type_field': '//*[@id="selautoType"]',
    'workloading_field': '//*[@id="caseViewForm_caseBO_workloading"]',
    'priority_field': '//*[@id="caseViewForm_caseBO_priorityName"]',
    'creator_field': '//*[@id="caseViewForm_caseBO_creator"]',
    'category_folder_field': '//*[@id="caseViewForm_caseBO_categoryName"]',
    'execution_type_field': '//*[@id="caseViewForm_caseBO_caseType"]',
    'status_field': '//*[@id="caseViewForm_caseBO_isactive"]',
    'os_field': '//*[@id="caseViewForm_osList"]',
    'phase_field': '//*[@id="caseViewForm_caseBO_selectedTags"]',
    'owner_field': '//*[@id="caseViewForm_caseBO_owner"]',
    'objective_field': '//*[@id="objectiveDiv"]',
    'release_notes_field': '//*[@id="descriptionDiv"]',
    #'type_matrix_field': '//*[@id="caseMatrix"]',
    'case_tools_field': '//*[@id="caseTool"]',
    #'attachments_field': '//*[@id="210195"]/td[1]/a',
}

folders = [
    ### ANDROID ###
    {
        #TC-4576PA
        'ids': ['menu_system_test', 'webfx-tree-object-3-plus', 'webfx-tree-object-4-plus', 'webfx-tree-object-5-plus', 'webfx-tree-object-6-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4602PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4604PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[3]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4575PA
        'ids': ['menu_system_test', 'webfx-tree-object-7-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]',
            **common_xpaths
        }
    },   
    {
        #TC-4595PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4542PA
        'ids': ['menu_system_test', 'webfx-tree-object-8-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4574PA
        'ids': ['menu_system_test', 'webfx-tree-object-9-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4616PA
        'ids': ['menu_system_test', 'webfx-tree-object-10-plus', 'webfx-tree-object-11-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4783PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
            **common_xpaths
        }
    },
    ### AOAC
    {
        #TC-5811PA
        'ids': ['menu_system_test', 'webfx-tree-object-12-plus', 'webfx-tree-object-13-plus', 'webfx-tree-object-14-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
            **common_xpaths
        }
    },
    ### APPLICATION ###
    {
        #TC-5313PA
        'ids': ['menu_system_test', 'webfx-tree-object-15-plus', 'webfx-tree-object-16-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5127PA
        'ids': ['menu_system_test', 'webfx-tree-object-17-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5128PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5131PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[3]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5202PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[4]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5332PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[5]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5419PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[6]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5632PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[7]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-5670PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[8]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-1542PA
        'ids': ['menu_system_test', 'webfx-tree-object-18-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            **common_xpaths
        }
    },
    {
        #TC-4579PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5245PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[3]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5379PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[4]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5380PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[5]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5392PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[6]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5421PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[7]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5652PA
        'ids': [],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[8]/td[1]',
            **common_xpaths
        }
    },
    {
        #TC-5669PA
        'ids': ['menu_system_test', 'webfx-tree-object-19-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
            **common_xpaths
        }
    },
    ### AUTO SCREEN ROTATION UTILITY ###
    {
        #TC-5651PA
        'ids': ['menu_system_test', 'webfx-tree-object-20-plus', 'webfx-tree-object-21-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
            **common_xpaths
        }
    },
    ### BATTERY ### ERR
    # {
    #     #TC-4284PA
    #     'ids': ['menu_system_test', 'webfx-tree-object-22-plus', 'webfx-tree-object-23-anchor'],
    #     'xpaths': {
    #         'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
    #         **common_xpaths
    #     }
    # },
    # {
    #     #TC-4455PA
    #     'ids': [],
    #     'xpaths': {
    #         'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
    #         **common_xpaths
    #     }
    # },
    # {
    #     #TC-5236PA
    #     'ids': [],
    #     'xpaths': {
    #         'navigate': '//*[@id="caseList"]/tbody/tr[3]/td[1]/a',
    #         **common_xpaths
    #     }
    # },
    # {
    #     #TC-4179PA
    #     'ids': ['menu_system_test', 'webfx-tree-object-24-anchor'],
    #     'xpaths': {
    #         'navigate': '//*[@id="caseList"]/tbody/tr/td[1]/a',
    #         **common_xpaths
    #     }
    # },
    ### COMPUTRACE ### ERR
    # {
    #     #TC-2917PA
    #     'ids': ['menu_system_test', 'webfx-tree-object-25-plus', 'webfx-tree-object-26-anchor'],
    #     'xpaths': {
    #         'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
    #         **common_xpaths
    #     }
    # },
    # {
    #     #TC-3986PA
    #     'ids': [],
    #     'xpaths': {
    #         'navigate': '//*[@id="caseList"]/tbody/tr[2]/td[1]/a',
    #         **common_xpaths
    #     }
    # },
    {
        ### DIGITIZER ###
        #TC-5302PA
        'ids': ['menu_system_test', 'webfx-tree-object-27-plus', 'webfx-tree-object-28-anchor'],
        'xpaths': {
            'navigate': '//*[@id="caseList"]/tbody/tr[1]/td[1]/a',
            **common_xpaths
        }
    },

]

# Loop through each folder to collect data
for folder in folders:
    data = navigate_and_collect_data(driver, folder['ids'], folder['xpaths'])

    # Create a temporary DataFrame for the current data
    temp_df = pd.DataFrame([{
        'Case ID': data['Case ID'],
        'Case type': data['Case type'],
        'Case name': data['Case name'],
        'Version': data['Version'],
        'Keywords': data['Keywords'],
        'Auto type': data['Auto type'],
        'Workloading': data['Workloading'],
        'Priority': data['Priority'],
        'Creator': data['Creator'],
        'Category folder': data['Category folder'],
        'Execution type': data['Execution type'],
        'Status': data['Status'],
        'OS': data['OS'],
        'Phase': data['Phase'],
        'Owner': data['Owner'],
        'Objective': data['Objective'],
        'Release notes': data['Release notes'],
        #'Type matrix': data['Type matrix'],
        'Case tools': data['Case tools'],
        #'Attachments': data['Attachments'],
    }])
    
    # Concatenate the current data with the main DataFrame
    df = pd.concat([df, temp_df], ignore_index=True)

# Print the gathered data
print(df)

# Specify the CSV file path
csv_file_path = 'TC_output.csv'

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

# Close the driver when done
time.sleep(3)
driver.quit()
print("Process Complete")