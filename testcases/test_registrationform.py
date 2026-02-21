import unittest

import pytest
from ddt import data, unpack

from pages.registrationform.registrationPage import RegistrationForm

@pytest.mark.usefixtures("setup")
class TestRegistrationForm(unittest.TestCase):

    @data(("Amar123", "amar@gmail","password123","Male","01/01/1990"))
    @unpack
    def test_registration_form(self,name,email,password,gender,date):
        register = RegistrationForm(self.driver)
        register.register_user(name,email,password,gender,date)
