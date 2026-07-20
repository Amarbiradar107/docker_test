# from base.BaseDriver import BaseDriver
import pytest
import allure
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

    @allure.step("Enter username")
    def getusername(self,username):
        self.wait_for_element_visible(By.XPATH, self.locator.username_input).send_keys(username)
    @allure.step("Enter email")
    def get_email(self,email):
        self.wait_for_element_visible(By.XPATH, self.locator.email_input).send_keys(email)
    @allure.step("Enter password")
    def get_password(self,password):
        self.wait_for_element_visible(By.XPATH, self.locator.password).send_keys(password)
    @allure.step("Click checkbox")
    def get_checkbox(self):
        self.wait_for_element_visible(By.XPATH, self.locator.checkbox).click()
    @allure.step("Get checkbox text")
    def get_checkbox_text(self):
        return self.wait_for_element_visible(By.XPATH, self.locator.checkbox_text).text
    @allure.step("Select gender")
    def get_gender_dropdown(self,male):
        return self.select_by_visible_text(By.XPATH,self.locator.gender_dropdown,male)
    @allure.step("Click employee radio button")
    def get_employee_radiobutton(self):
        return self.wait_for_element_visible(By.XPATH, self.locator.employee_radiobutton).click()
    @allure.step("Enter date in calendar")
    def get_calendar(self,date):
        return self.enter_text(By.XPATH, self.locator.calendar,date)
    @allure.step("Click submit button")
    def get_submit_button(self):
        return self.wait_for_element_visible(By.XPATH, self.locator.submit_button).click()
    @allure.step("Get success message")
    def get_success_message(self,expected_text):
        actual_text = self.wait_for_element_visible(By.XPATH, self.locator.success_message).text.split("\n")
        self.assert_equal(actual_text[1],expected_text)

    def register_user(self,testdata):
        self.getusername(testdata[0])
        self.get_email(testdata[1])
        self.get_password(testdata[2])
        self.get_checkbox()
        # print("successfully registered user with username: {}, email: {}, password: {}".format(testdata[0], testdata[1], testdata[2]))
        self.get_gender_dropdown(testdata[3])
        self.get_employee_radiobutton()
        self.get_calendar("01-01-1990")
        self.get_submit_button()
        self.get_success_message(expected_text="Success! The Form has been submitted successfully!.")
        self.scroll_to_element(By.XPATH, self.locator.success_message)
        self.take_screenshot("screenshots/registration_success.png")



        # GenderSelection = Select(self.wait_for_element_visible("xpath", self

