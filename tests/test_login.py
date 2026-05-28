import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup_and_teardown")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    def test_valid_login(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.NAME,"email").send_keys("qwert@gamil.com")
        time.sleep(1)
        self.driver.find_element(By.ID,"input-password").send_keys("123@123")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
        time.sleep(3)
    def test_invalid_login(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.NAME, "email").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.ID, "input-password").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").is_displayed()
        time.sleep(3)

