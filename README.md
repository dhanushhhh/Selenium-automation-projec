# Selenium Automation Project

## Overview

![Project Logo](logo_small.png)

This project involves automating the testing of the website [The Sparks Foundation Singapore](https://www.thesparksfoundationsingapore.org/) using Selenium. The goal is to automate various interactions and tests on the website as part of an internship task.


## Homepage
-  [title.py](title.py) `title.py` - This code snippet utilizes Selenium WebDriver to open a webpage, retrieve its title, and print it.
-  [check_footer_visibility.py](check_footer_visibility.py) `check_footer_visibility.py` - This code snippet utilizes Selenium WebDriver to open a webpage and scroll down to the footer. 
-  [check_logo_presence.py](check_logo_presence.py) `check_logo_presence.py` - This code snippet utilizes Selenium WebDriver to navigate to a website and find the logo element. 
-  [extract_company_name.py](extract_company_name.py) `extract_company_name.py` - This code snippet utilizes Selenium WebDriver to navigate to a website and find the organisation name element.


## About Us page
-  [about_info.py](about_info.py) `about_info.py` - This code snippet utilizes Selenium WebDriver to navigate to the About Us page of a website and extract the Vision, Mission, and Values information. It clicks on the 'About Us' link, then clicks on the 'Vision, Mission and Values' link. After highlighting the title element using JavaScript, it extracts and prints the Vision Statement, Mission Statement, and Our Values.


## Contact Us page
-  [join_tsf_network.py](join_tsf_network.py) `join_tsf_network.py` - This code snippet utilizes Selenium WebDriver to navigate to a website and click on the 'Contact Us' link. It then finds the 'Join TSF Network' link on the Contact Us page and retrieves its URL. The URL is printed to simulate the action of joining the group on LinkedIn. Finally, the browser window is closed.

-  [extract_email_address.py](extract_email_address.py) `extract_email_address.py` - This code snippet utilizes Selenium WebDriver to navigate to a website and click on the 'Contact Us' link. It then extracts and highlights the email address displayed on the Contact Us page using JavaScript. The email address is then extracted from the element's text using regular expressions. Finally, the email address is printed in a format resembling a mailto link.


## Join Us page
-  [join_form_submission.py](join_form_submission.py) `join_form_submission.py` - To automate form submission using Selenium WebDriver for web testing or data collection purposes.
-  [highlight_internship_title.py](highlight_internship_title.py) `highlight_internship_title.py` - This code snippet demonstrates the automation of extracting and highlighting the title of the Graduate Rotational Internship Program on the website of The Sparks Foundation Singapore. It uses Selenium WebDriver to navigate to the Internship Positions page, locate the title element, and highlight it using JavaScript.


## Policies page
- [click_and_highlight_policy_summary.py](click_and_highlight_policy_summary.py) `click_and_highlight_policy_summary.py` - This code snippet can be included in a GitHub README to demonstrate how to automate the extraction and highlighting of specific content (in this case, the policy summary) from a webpage using Selenium WebDriver.


## Installation

### Prerequisites
- Python: [Download Python](https://www.python.org/downloads/)
- Google Chrome: [Download Chrome](https://www.google.com/chrome/)

### Dependencies
1. Install Selenium:
    ```
    pip install selenium
    ```

2. Download ChromeDriver:
    - Download ChromeDriver from the [ChromeDriver download page](https://chromedriver.chromium.org/downloads).
    - Extract the downloaded file and place the `chromedriver` executable in your system PATH.

### Running the Project

- Run the Python script:
    ```
    python script_name.py
    ```

