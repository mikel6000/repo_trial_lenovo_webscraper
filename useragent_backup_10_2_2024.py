import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Access credentials directly from environment variables
username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Initialize Chrome options and set user agent
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
chrome_options.add_argument("--incognito")
# chrome_options.add_argument('--log-level=3')
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')

# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
# options.add_argument("--incognito")
# options.add_argument('--log-level=3')
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')

# Use the credentials to log in
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'loginsub').click()
# driver.implicitly_wait(10)

# Wait for a few seconds to observe the result
time.sleep(5)
driver.quit()
print("Process Complete")