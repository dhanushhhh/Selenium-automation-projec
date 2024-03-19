import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup
driver = webdriver.Chrome()

# Open your website
driver.get("https://www.thesparksfoundationsingapore.org/")

# Navigate to the Contact Us page
contact_us_link = driver.find_element(By.XPATH, '//a[@data-hover="Contact Us"]')
contact_us_link.click()
time.sleep(2)  # Wait for 2 seconds

# Find the "Join TSF Network" link on the Contact Us page
join_network_link = driver.find_element(By.XPATH, '//a[contains(text(), "JOIN TSF NETWORK HERE")]')

# Get the URL of the link
join_network_url = join_network_link.get_attribute("href")

# Print a message indicating the action
print("Simulating joining the group on LinkedIn with the following link:")
print(join_network_url)

# Quit the browser
driver.quit()
