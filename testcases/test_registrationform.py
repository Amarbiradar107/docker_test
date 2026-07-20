import pytest
import allure

from pages.registrationform.registrationPage import RegistrationForm
from utilites.excelutil import ExcelUtil
import logging

test_data_path = "testdata/testData.xlsx"
read_excel = ExcelUtil.read_excel(test_data_path,"testdata")

class TestRegistrationForm:

    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    @allure.feature("Login")
    @allure.story("Valid Login")
    @allure.title("Verify user can login successfully")
    @pytest.mark.parametrize("testdata",read_excel)
    def test_registration_form(self,setup,testdata):
        self.driver = setup
        self.log.info(f"test data : {testdata}")
        register = RegistrationForm(self.driver)
        register.register_user(testdata)
