import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.thesparksfoundationsingapore.org/")

# Wait for the page to load
time.sleep(2)

# Find the company name element
company_name_element = driver.find_element(By.XPATH, '//a[@class="col-md-6 navbar-brand"]')

# Highlight the company name using JavaScript
driver.execute_script("arguments[0].setAttribute('style', 'background-color: black; border: 2px white;');", company_name_element)

# Wait for 3 seconds to see the highlighted company name
time.sleep(3)

# Extract the text of the company name
company_name = company_name_element.text

# Print the company name
print("\nOrganisation Name:\n", company_name)

# Quit the browser
driver.quit()
