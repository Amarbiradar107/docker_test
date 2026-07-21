import pytest
from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup(request):
    # driver = webdriver.Chrome()
    options = Options()
    driver = webdriver.Remote(
        command_executor="http://selenium-hub:4444/wd/hub",
        options=options
    )
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=AttachmentType.PNG
            )