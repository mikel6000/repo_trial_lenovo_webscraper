from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set download directory and preferences
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "/path/to/download",  # Change to your desired download path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_setting_values.automatic_downloads": 1,
    "profile.default_content_setting_values.mixed_script": 1  # Allow mixed content
}
options.add_experimental_option("prefs", prefs)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the URL and perform download actions
driver.get("your_download_page_url")

# Make sure to interact with the page to trigger the download
# e.g., clicking the download link/button
