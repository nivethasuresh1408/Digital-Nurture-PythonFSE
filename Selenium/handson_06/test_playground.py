import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# -------------------------------------------------
# Task 45
# -------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    message_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "user-message"))
    )

    message_box.clear()
    message_box.send_keys(message)

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )

    driver.execute_script("arguments[0].click();", button)

    output = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert output.text.strip() == message


# -------------------------------------------------
# Task 43
# -------------------------------------------------

def test_checkbox_demo(driver, base_url):

    driver.get(base_url + "checkbox-demo")

    checkbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='checkbox']")
        )
    )

    driver.execute_script("arguments[0].click();", checkbox)

    assert checkbox.is_selected()


# -------------------------------------------------
# Task 49
# -------------------------------------------------

def test_dropdown_selection(driver, base_url):

    driver.get(base_url + "select-dropdown-demo")

    dropdown = Select(
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "select-demo"))
        )
    )

    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"