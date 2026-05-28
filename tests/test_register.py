import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_all_filelds(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("abcde")
        self.driver.find_element(By.NAME, "lastname").send_keys("defghij")
        self.driver.find_element(By.NAME, "email").send_keys(timestamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("123456789")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234@1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("1234@1234")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        exp_output="Your Account Has Been Created!"
        out_put=self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        print(out_put)
        assert out_put==exp_output
    def test_register_with_no_filelds(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("abcde")
        self.driver.find_element(By.NAME, "lastname").send_keys("defghij")
        self.driver.find_element(By.NAME, "email").send_keys(timestamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234@1234")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("1234@1234")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text=="Your Account Has Been Created!"

def timestamp():
    from datetime import datetime
    current_time = datetime.now().strftime("%H_%M_%S")
    return current_time+"@gmail.com"
