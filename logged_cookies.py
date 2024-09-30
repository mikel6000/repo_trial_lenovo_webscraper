#script for automating a webpage that is ALREADY logged in, and will also use cookies.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
chrome_options.add_argument("--incognito")
# chrome_options.add_argument('--log-level=3')
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

#Access website and login
# driver.get('http://tdms.lenovo.com/tdms/loginAction!login.do')
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')

# Save cookies after logging in manually
time.sleep(20)

# Retrieve cookies
cookies = driver.get_cookies()

# Quit the driver
driver.quit()

# Reinitialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')

# Add cookies to the new session
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to reflect the logged-in status
driver.refresh()

# Add/perform automated actions on the logged-in website
time.sleep(5)
test_menu = driver.find_element(By.ID, 'menu_system_test').click()

# Close the driver when done
driver.quit()