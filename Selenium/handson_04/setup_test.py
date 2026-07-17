"""
====================================================
Hands-on 04
Task 24: Selenium Architecture
====================================================

1. WebDriver
   - WebDriver is the main Selenium component used to automate web browsers.
   - It communicates directly with the browser and executes commands sent from Python.

2. Selenium Grid
   - Selenium Grid allows tests to run on multiple browsers and machines in parallel.
   - It is mainly used for cross-browser and distributed testing.

3. Selenium IDE
   - Selenium IDE is a browser extension.
   - It is used for record-and-playback testing and can generate automation scripts.

====================================================
Task 25:
Open Chrome, navigate to LambdaTest Selenium Playground,
print the page title, and close the browser.

Task 26:
Implicit Wait is added globally.
Explicit Waits are preferred because they wait only for
specific elements, making tests faster and more reliable.

Task 27:
Browser is executed in Headless Mode.
====================================================
"""

from selenium import webdriver

# Chrome Options
options = webdriver.ChromeOptions()

# Run browser in Headless Mode
options.add_argument("--headless=new")

# Launch Chrome Browser
driver = webdriver.Chrome(options=options)

# Global Implicit Wait
driver.implicitly_wait(10)

# Open LambdaTest Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print Page Title
print("Page Title:", driver.title)

# Close Browser
driver.quit()