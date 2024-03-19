import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")

# Click on the "Join Us" dropdown element
join_us_dropdown = driver.find_element(By.XPATH, '//a[@data-hover="Join Us"]')
join_us_dropdown.click()

# Find and click on the "Internship Positions" link in the dropdown
internship_positions_link = driver.find_element(By.XPATH, '//a[@href="/join-us/internship-positions/"]')
internship_positions_link.click()

# Wait for the page to load
time.sleep(3)

# Find the title element of the internship
title_element = driver.find_element(By.XPATH, '//span[text()="Graduate Rotational Internship Program"]')

# Highlight the title using JavaScript
driver.execute_script("arguments[0].style.backgroundColor = 'black'; arguments[0].style.border = '2px white';", title_element)

# Wait for 3 seconds to show the highlighted title
time.sleep(3)

# Print the title
print("Internship Title:", title_element.text)

# Quit the browser
driver.quit()
