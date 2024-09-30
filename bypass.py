#trial for bypass scraping (already logged in)
#trial for getting necessary web components/elements

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('http://tdms.lenovo.com/tdms/loginAction!login.do')
# driver.get('http://tdms.lenovo.com/tdms/homeAction.action?sysPageId=page_common_home')

# Close the driver when done
time.sleep(3)
driver.quit()
print("Process Complete")
