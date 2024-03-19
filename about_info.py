import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")

# Click on "About Us" link
about_us_link = driver.find_element(By.LINK_TEXT, "About Us")
about_us_link.click()
time.sleep(2)  # Wait for 2 seconds

# Click on "Vision, Mission and Values" link
vision_mission_values_link = driver.find_element(By.XPATH, '//a[@href="/about/vision-mission-and-values/"]')
vision_mission_values_link.click()
time.sleep(2)  # Wait for 2 seconds

# Execute JavaScript to highlight the <h2> element
driver.execute_script('document.querySelector(".inner-tittle-w3layouts").setAttribute("style", "background-color: black; border: 2px white;");')

# Find the element containing the Vision Statement
vision_statement_element = driver.find_element(By.XPATH, '//h3[contains(@class, "tittle-agileits-w3layouts") and contains(span/text(), "Our Vision Statement")]/following-sibling::div[contains(@class, "media")]/div[contains(@class, "media-body")]/p')
vision_statement_text = vision_statement_element.text.strip()
print("\nVision Statement: ", vision_statement_text)
time.sleep(2)  # Wait for 2 seconds
print()  # Empty line

# Find the element containing the Mission Statement
mission_statement_element = driver.find_element(By.XPATH, '//h3[contains(@class, "tittle-agileits-w3layouts") and contains(span/text(), "Our Mission Statement")]/following-sibling::div[contains(@class, "media")]/div[contains(@class, "media-body")]/p')
mission_statement_text = mission_statement_element.text.strip()
print("Mission Statement: ", mission_statement_text)
time.sleep(2)  # Wait for 2 seconds
print()  # Empty line

# Find the elements containing the Values
values_elements = driver.find_elements(By.XPATH, '//h3[contains(@class, "tittle-agileits-w3layouts") and contains(span/text(), "Our Values")]/following-sibling::div[contains(@class, "media")]//div[contains(@class, "media-body")]')
print("\nOur Values: \n")
for value_element in values_elements:
    value_text = value_element.text.strip()
    # If there are multiple lines in the value, split them and print each line separately
    for line in value_text.split('\n'):
        print(line)
    time.sleep(2)  # Wait for 2 seconds
    print()  # Empty line

# Quit the browser
driver.quit()

# Print success message
print("Extraction of Vision, Mission, and Values from About Us successful!")
