import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

relative_chromedriver_path = './Driver/chromedriver.exe'

dir = os.path.dirname(__file__)
chromedriver_path = os.path.join(dir, relative_chromedriver_path)

# Boolean variable to control headless mode
headless_mode = False

def initialize_webdriver(driver_path, headless=False):
    try:
        print("Initializing WebDriver...")
        options = Options()

        if headless:
            options.add_argument('--headless')

        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        if headless:
            print("-- WebDriver initialized in headless mode. --")
        else:
            print("-- WebDriver initialized successfully. --")
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        raise
    


def main():

    driver_path = chromedriver_path
    web_url = 'https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do'

    # Initialize WebDriver
    driver = initialize_webdriver(driver_path, headless=headless_mode)

    # Open the login page
    driver.get(web_url)

    # Wait for a few seconds to allow for manual login
    print("Please enter your login credentials manually. Once done, press Enter to continue...")
    input()  # Wait for the user to press Enter

    # Optionally, wait for the page to load after login
    time.sleep(30)

    # Continue with the automated process
    ###

    # Close the driver when done
    driver.quit()

if __name__ == "__main__":
    main()