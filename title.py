from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Set an implicit wait for 10 seconds
driver.implicitly_wait(10)

# Navigate to a website
driver.get('https://www.thesparksfoundationsingapore.org/')

# Get the website title
title = driver.title
print("\nWebsite Title:\n", title)

# Close the browser
driver.quit()
