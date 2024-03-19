import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")

# Click on "Policies and Code" dropdown
dropdown_toggle = driver.find_element(By.XPATH, '//a[@data-hover="Policies and Code"]')
dropdown_toggle.click()

# Click on "Policies" link
policies_link = driver.find_element(By.XPATH, '//a[@href="/policies-and-code/policies/"]')
policies_link.click()

# Wait for the page to load
time.sleep(3)

# Find and highlight the policy summary
policy_summary = driver.find_element(By.XPATH, '//span[text()="Summary of important Policies at The Sparks Foundation"]')
driver.execute_script("arguments[0].setAttribute('style', 'background-color: black; border: 2px white;');", policy_summary)

# Print the highlighted policy summary
print("\nHighlighted Policy Summary:\n", policy_summary.text)

# Wait for 3 seconds to show the highlighted summary
time.sleep(3)

# Quit the browser
driver.quit()
