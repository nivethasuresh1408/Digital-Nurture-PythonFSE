"""
====================================================
Hands-on 04
Task 28–31
WebDriver Navigation, Windows & Screenshots
====================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Browser
driver = webdriver.Chrome()

# Maximize Browser
driver.maximize_window()

# Open LambdaTest Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

time.sleep(2)

# Navigate to Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("Navigation Successful")

# Navigate Back
driver.back()

time.sleep(2)

# Open Google in a New Tab
driver.execute_script("window.open('https://www.google.com');")

# Print Window Handles
print("Window Handles:", driver.window_handles)

# Switch to Google Tab
driver.switch_to.window(driver.window_handles[1])

# Print Google Title
print("Google Title:", driver.title)

# Switch Back to Selenium Playground
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

# Take Screenshot
driver.save_screenshot("playground_screenshot.png")

print("Screenshot Saved Successfully")

# Display Window Size
print("Current Window Size:", driver.get_window_size())

# Set Window Size
driver.set_window_size(1280, 800)

# Consistent browser window size helps ensure
# responsive web pages behave consistently
# across different executions.

print("Window resized to 1280 x 800")

# Close Browser
driver.quit()