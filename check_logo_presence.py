import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.thesparksfoundationsingapore.org/")

# Wait for the page to load
time.sleep(2)

# Find the logo element
logo_element = driver.find_element(By.XPATH, '//img[@src="/images/logo_small.png"]')

# Highlight the logo using JavaScript
driver.execute_script("arguments[0].setAttribute('style', 'border: 2px solid black;');", logo_element)

# Wait for 3 seconds to see the highlighted logo
time.sleep(3)

# Check if the logo is displayed
if logo_element.is_displayed():
    print("\nSuccess: Logo found on the website.\n")
else:
    print("Failure: Logo not found on the website.")

# Quit the browser
driver.quit()
