from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the WebDriver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the webpage
driver.get('URL_OF_YOUR_PAGE')

# Specify the range of numbers for your IDs
start_num = 1  # Adjust based on your needs
end_num = 10   # Adjust based on your needs

# List to hold the retrieved data
data = []

# Step 1: Loop through the specified range to find and click each dropdown/plus icon
for i in range(start_num, end_num + 1):
    element_id = f"webfx-tree-object-{i}-plus"
    
    try:
        # Wait for the element to be present and clickable by ID
        icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element_id)))
        
        # Scroll to the element if it's not in the viewport
        ActionChains(driver).move_to_element(icon).perform()
        
        # Click the icon
        icon.click()
        
        # Optionally wait for the dropdown to expand
        WebDriverWait(driver, 2)  # Adjust based on your needs

    except Exception as e:
        print(f"Could not click icon with ID {element_id}: {e}")
        continue  # Continue to the next element

# Step 2: List of XPaths to click after expanding icons
xpaths_to_click = [
    "//div[@class='your-target-class-1']",  # Adjust these XPaths as needed
    "//div[@class='your-target-class-2']",
    "//div[@class='your-target-class-3']",
    # Add more XPaths as necessary
]

# Step 3: Loop through each XPath to click and retrieve data
for xpath in xpaths_to_click:
    try:
        # Wait for the target element to be clickable
        target_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        
        # Scroll to the target element
        ActionChains(driver).move_to_element(target_element).perform()
        
        # Click the target element
        target_element.click()

        # Wait for values to be retrievable (adjust selectors as necessary)
        value_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='value-class']")))  # Adjust this XPath
        
        # Extract values
        values = [value_elem.text for value_elem in value_elements]  # Get the text values

        # Append the retrieved values to the data list
        data.append({'xpath': xpath, 'values': values})

    except Exception as e:
        print(f"Could not click the target element with XPath {xpath}: {e}")
        continue  # Continue to the next XPath

# Create a DataFrame from the retrieved data
df = pd.DataFrame(data)

# Display or save the DataFrame
print(df)
# Optionally save to a CSV file
# df.to_csv('output.csv', index=False)

# Close the browser
driver.quit()
