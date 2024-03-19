import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.thesparksfoundationsingapore.org/")

# Navigate to the Contact Us page
contact_us_link = driver.find_element(By.XPATH, '//a[@data-hover="Contact Us"]')
contact_us_link.click()
time.sleep(2)  # Wait for 2 seconds

# Find the email address element
email_element = driver.find_element(By.XPATH, '//p[contains(text(), "info@thesparksfoundation.sg")]')

# Highlight the email address using JavaScript
driver.execute_script("arguments[0].style.backgroundColor = 'blue'; arguments[0].style.border = '2px black';", email_element)

# Extract only the email address from the email element
email_text = email_element.text.strip()
email_address = re.search(r'[\w\.-]+@[\w\.-]+', email_text).group()

# Print a message indicating the action to simulate clicking on the email address
print("Simulating clicking on the email address to send an email to:", email_address)

# Wait for 3 seconds to show the highlighted email
time.sleep(3)

# Print the email address in a format that resembles a mailto link
print("mailto:" + email_address)

# Quit the browser
driver.quit()

