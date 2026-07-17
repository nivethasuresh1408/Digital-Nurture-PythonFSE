"""
Hands-on 05
Task 32-35
Locator Strategies
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# ------------------------------
# ID Locator
# ------------------------------
element = driver.find_element(By.ID, "user-message")
print("Located using ID")

# ------------------------------
# NAME Locator
# ------------------------------
element = driver.find_element(By.NAME, "message")
print("Located using NAME")

# ------------------------------
# CLASS Locator
# ------------------------------
element = driver.find_element(By.CLASS_NAME, "form-control")
print("Located using CLASS")

# ------------------------------
# TAG Locator
# ------------------------------
element = driver.find_element(By.TAG_NAME, "input")
print("Located using TAG")

# ------------------------------
# Absolute XPath
# (Not Recommended)
# ------------------------------

try:
    element = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/section[1]/div/div/div[1]/div/input"
    )
    print("Located using Absolute XPath")
except:
    print("Absolute XPath may differ.")

# ------------------------------
# Relative XPath
# ------------------------------

element = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("Located using Relative XPath")

# ------------------------------
# CSS Selector by ID
# ------------------------------

driver.find_element(By.CSS_SELECTOR, "#user-message")

print("CSS by ID")

# ------------------------------
# CSS by Attribute
# ------------------------------

driver.find_element(
    By.CSS_SELECTOR,
    "input[name='message']"
)

print("CSS by Attribute")

# ------------------------------
# CSS Parent Child
# ------------------------------

try:
    driver.find_element(
        By.CSS_SELECTOR,
        "div.w-6 > input"
    )
    print("CSS Parent Child")
except:
    print("Parent Child selector may vary depending on page structure.")

# ------------------------------
# Checkbox Demo
# ------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print(label.text)

labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Total Option Labels:", len(labels))
# ------------------------------------
# Locator Ranking
# ------------------------------------
# 1. ID
# 2. CSS Selector
# 3. Name
# 4. Relative XPath
# 5. Class Name
# 6. Absolute XPath
#
# Reason:
# ID is unique and fastest.
# CSS Selectors are readable and fast.
# Absolute XPath breaks whenever the page structure changes.

driver.quit()