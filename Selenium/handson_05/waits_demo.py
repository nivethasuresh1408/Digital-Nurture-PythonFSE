"""
Hands-on 05
Task 36-39
Explicit Waits
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

# -------------------------------
# Explicit Wait
# -------------------------------

driver.find_element(By.ID, "autoclosable-btn-success").click()

wait = WebDriverWait(driver,10)

alert = wait.until(

    EC.visibility_of_element_located(

        (By.CSS_SELECTOR,".alert-success")

    )

)

assert "successfully" in alert.text.lower()

print("Explicit Wait Successful")

# -------------------------------
# time.sleep()
# -------------------------------

start = time.time()

driver.refresh()

driver.find_element(By.ID,"autoclosable-btn-success").click()

time.sleep(3)

end = time.time()

print("Sleep Time:",end-start)

# -------------------------------
# Explicit Wait Timing
# -------------------------------

driver.refresh()

start = time.time()

driver.find_element(By.ID,"autoclosable-btn-success").click()

wait.until(

    EC.visibility_of_element_located(

        (By.CSS_SELECTOR,".alert-success")

    )

)

end = time.time()

print("Explicit Wait:",end-start)

# -------------------------------
# Clickable Wait
# -------------------------------

button = wait.until(

    EC.element_to_be_clickable(

        (By.ID,"autoclosable-btn-success")

    )

)

button.click()

"""
visibility_of_element_located

Element is visible.

element_to_be_clickable

Element is visible

AND

Enabled

AND

Clickable
"""

# -------------------------------
# Fluent Wait
# -------------------------------

fluent_wait = WebDriverWait(

    driver,

    timeout=10,

    poll_frequency=0.5,

    ignored_exceptions=[NoSuchElementException]

)

print("Fluent Wait Configured")

driver.quit()