from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SimpleFormPage(BasePage):

    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.ID, "showInput")
    DISPLAY_MESSAGE = (By.ID, "message")

    def enter_message(self, text):
        box = self.wait_for_element(self.MESSAGE_INPUT)
        box.clear()
        box.send_keys(text)

    def click_submit(self):
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def get_displayed_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.DISPLAY_MESSAGE)
        )
        return self.driver.find_element(*self.DISPLAY_MESSAGE).text