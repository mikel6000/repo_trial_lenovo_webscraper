#Type 'navigator.userAgent' in the developer's tool console tab and press enter

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Access credentials directly from environment variables
username = os.getenv('zlen_username')
password = os.getenv('zlen_password')

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
opts = Options()
# opts.add_argument("user-agent=Chrome/39.0.2171.95")
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
# driver = webdriver.Chrome(chrome_options=opts)
driver = webdriver.Chrome(service=service, options=opts)
driver.maximize_window()
driver.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')
# driver.implicitly_wait(3)

# Use the credentials to log in
username_textbox = driver.find_element(By.ID, 'username').send_keys(f'{username}')
password_textbox = driver.find_element(By.ID, 'password').send_keys(f'{password}')
# driver.find_element(By.ID, 'loginsub').send_keys(Keys.ENTER)
# driver.find_element(By.ID, 'loginsub').click()
driver.implicitly_wait(10)

# Close the driver when done
time.sleep(3)
driver.quit()
print("Process Complete")