import time
from selenium import webdriver

# Setup
driver = webdriver.Chrome()
driver.get("https://www.thesparksfoundationsingapore.org/")

# Scroll down to the footer
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for 3 seconds to allow time for scrolling
time.sleep(3)

# Print a success message
print("\nFooter displayed successfully.\n")

# Quit the browser
driver.quit()
