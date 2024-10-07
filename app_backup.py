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

# Set Chrome options1
# chrome_options = webdriver.ChromeOptions()
# chrome_options.enable_downloads = True

# # Add download preferences
# prefs = {
#     "download.default_directory": target,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True,
#     "safebrowsing.disable_download_protection": True
# }

# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.enable_downloads = True
# chrome_options.add_argument("--enable-managed-downloads true")


# Set Chrome options2
# chrome_options = Options()
# chrome_options.add_experimental_option("prefs", {
#     "download.default_directory": "C:/Users/michaeljohn.roguel/Documents/GitHub/repo_trial_lenovo_webscraper/Downloads",
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True,
#     "safebrowsing.disable_download_protection": True,
# })
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode
# # chrome_options.add_argument("--no-sandbox")
# # chrome_options.add_argument("--disable-dev-shm-usage")
# # chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration

# Set chrome option3
chrome_options = Options()
for arg in ["--unsafely-treat-insecure-origin-as-secure=http://tdms.lenovo.com/"]:
    chrome_options.add_argument(arg)
# for arg in ["--allow-running-insecure-content", "--disable-web-security", "--disable-features=InsecureDownloadWarnings", ]:
#     chrome_options.add_argument(arg)

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')


# Use the credentials to log in
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'loginsub').click()
driver.refresh()

#Navigate to the Test case DB
driver.find_element(By.ID, 'menu_system_test').click()
driver.find_element(By.ID, 'webfx-tree-object-3-plus').click()
driver.find_element(By.ID, 'webfx-tree-object-4-plus').click()
driver.find_element(By.ID, 'webfx-tree-object-5-plus').click()
driver.find_element(By.ID, 'webfx-tree-object-6-anchor').click()
driver.find_element(By.XPATH, '//*[@id="caseList"]/tbody/tr[1]/td[1]/a').click()

#Get the data
# case_type = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[1]/td[1]').text
# case_type_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_caseClassName"]').get_attribute("value")
# print(f'{case_type} {case_type_field}')

# case_id = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[1]/td[5]').text
# case_id_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_caseAlias"]').get_attribute("value")
# print(f'{case_id} {case_id_field}')

# case_name = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[2]/td[1]').text
# case_name_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_caseName"]').get_attribute("value")
# print(f'{case_name} {case_name_field}')

# category_folder = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[2]/td[5]').text
# category_folder_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_categoryName"]').get_attribute("value")
# print(f'{category_folder} {category_folder_field}')

# version = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[3]/td[1]').text
# version_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_version"]').get_attribute("value")
# print(f'{version} {version_field}')

# execution_type = driver.find_element(By.XPATH, '//*[@id="basicdiv"]/table/tbody/tr[3]/td[5]').text
# execution_type_field = driver.find_element(By.XPATH, '//*[@id="caseViewForm_caseBO_caseType"]').get_attribute("value")
# print(f'{execution_type} {execution_type_field}')


attachment = driver.find_element(By.XPATH, '//*[@id="210195"]/td[1]/a').click()
#target = "C:/Users/michaeljohn.roguel/Documents/GitHub/repo_trial_lenovo_webscraper/Downloads"
# driver.get_downloadable_files()
# driver.download_file(attachment, target)
#print(f'The attachement file {attachment} is downloaded and saved to Downloads directory')

# Close the driver when done
time.sleep(5)
driver.quit()
# print("Process Complete")