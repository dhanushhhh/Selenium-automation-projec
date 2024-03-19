import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Setup
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")

# Click on the "Join Us" dropdown element
join_us_dropdown = driver.find_element(By.XPATH, '//a[@data-hover="Join Us"]')
join_us_dropdown.click()

# Find and click on the "Why Join Us" link in the dropdown
why_join_us_link = driver.find_element(By.XPATH, '//a[@href="/join-us/why-join-us/"]')
why_join_us_link.click()

# Define the expected URL of the "Why Join Us" page
expected_url = driver.current_url

# Fill the form fields
name_input = driver.find_element(By.NAME, "Name")
name_input.send_keys("John Doe")

email_input = driver.find_element(By.NAME, "Email")
email_input.send_keys("johndoe@example.com")

role_select = Select(driver.find_element(By.CSS_SELECTOR, "select.form-control"))
role_select.select_by_visible_text("Student")

# Submit the form
submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_button.click()

# Delay to see the form submission
time.sleep(3)

# Optional: Verify if the form was submitted successfully
current_url = driver.current_url
if current_url != expected_url:
    print("Successfully submitted the form.")
else:
    print("Failed to submit the form.")

# Quit the browser
driver.quit()
