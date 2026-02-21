from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import logging


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5
        self.log = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    def wait_for_element_clickable(self, by_type, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll_frequency)
            return wait.until(EC.element_to_be_clickable((by_type, locator)))
        except TimeoutException:
            self.log.error(f"Element not clickable: {locator}")
            return None

    def wait_for_element_visible(self, by_type, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll_frequency)
            return wait.until(EC.visibility_of_element_located((by_type, locator)))
        except TimeoutException:
            self.log.error(f"Element not visible: {locator}")
            return None

    def select_by_visible_text(self, by_type, locator, text):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            Select(element).select_by_visible_text(text)
            print("Selected option by visible text:", text)

    def select_by_value(self, by_type, locator, value):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            Select(element).select_by_value(value)

    def select_by_index(self, by_type, locator, index):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            Select(element).select_by_index(index)

    def get_all_dropdown_options(self, by_type, locator):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            select = Select(element)
            return [option.text for option in select.options]
        return []

    def get_selected_option(self, by_type, locator):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            select = Select(element)
            return select.first_selected_option.text
        return None

    def enter_text(self, by_type, locator, text):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            element.clear()
            element.send_keys(text)
            print(f"Entered text: {text} in element: {locator}")
        else:
            self.log.error(f"Failed to enter text in element: {locator}")

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def scroll_to_element(self, by_type, locator):
        element = self.wait_for_element_visible(by_type, locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
