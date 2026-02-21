# from base.BaseDriver import BaseDriver
import pytest
from selenium.webdriver.common.by import By

from base.BaseDriver import BaseDriver
from locators.registration_form.registration import RegistrationFormLocator
from utilites.Assertions import Assertions


@pytest.mark.usefixtures("setup")
class RegistrationForm(BaseDriver,Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = RegistrationFormLocator()

    def getusername(self,username):
        self.wait_for_element_visible(By.XPATH, self.locator.username_input).send_keys(username)
    def get_email(self,email):
        self.wait_for_element_visible(By.XPATH, self.locator.email_input).send_keys(email)
    def get_password(self,password):
        self.wait_for_element_visible(By.XPATH, self.locator.password).send_keys(password)
    def get_checkbox(self):
        self.wait_for_element_visible(By.XPATH, self.locator.checkbox).click()
    def get_checkbox_text(self):
        return self.wait_for_element_visible(By.XPATH, self.locator.checkbox_text).text
    def get_gender_dropdown(self,male):
        return self.select_by_visible_text(By.XPATH,self.locator.gender_dropdown,male)
    def get_employee_radiobutton(self):
        return self.wait_for_element_visible(By.XPATH, self.locator.employee_radiobutton).click()
    def get_calendar(self,date):
        return self.enter_text(By.XPATH, self.locator.calendar,date)
    def get_submit_button(self):
        return self.wait_for_element_visible(By.XPATH, self.locator.submit_button).click()
    def get_success_message(self,expected_text):
        actual_text = self.wait_for_element_visible(By.XPATH, self.locator.success_message).text.split("\n")
        self.assert_equal(actual_text[1],expected_text)

    def register_user(self,username,email,password,male,date):
        self.getusername(username)
        self.get_email(email)
        self.get_password(password)
        self.get_checkbox()
        print("successfully registered user with username: {}, email: {}, password: {}".format(username, email, password))
        self.get_gender_dropdown(male)
        self.get_employee_radiobutton()
        self.get_calendar(date)
        self.get_submit_button()
        self.get_success_message(expected_text="Success! The Form has been submitted successfully!.")
        self.scroll_to_element(By.XPATH, self.locator.success_message)
        self.take_screenshot("screenshots/registration_success.png")



        # GenderSelection = Select(self.wait_for_element_visible("xpath", self

