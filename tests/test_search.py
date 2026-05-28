import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_valid_search(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_invalid_search(self):
        self.driver.find_element(By.NAME, "search").send_keys("honda")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        time.sleep(2)
        expected_title="Products meeting the search criteria"
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::h2").text==expected_title


