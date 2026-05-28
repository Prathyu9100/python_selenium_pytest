import pytest
from selenium import webdriver
from urllib3 import request
import allure

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def setup_and_teardown(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        driver=webdriver.Chrome()
    if browser=="edge":
        driver=webdriver.Edge()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()
# Hook for screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Take screenshot only when test fails
    if report.when == "call" and report.failed:

        driver = item.cls.driver

        allure.attach(
            driver.get_screenshot_as_png(),
            name="failed_test",)
