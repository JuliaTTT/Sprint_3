import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import mylocators
import myconsts


@pytest.mark.usefixtures("start_for_login")
class TestConstructor:

    def login(self):
        self.driver.find_element(By.XPATH, mylocators.email).send_keys(myconsts.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(myconsts.password)
        self.driver.find_element(By.XPATH, mylocators.enter).click()

    def test_constructor_from_personal_account(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.login()
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.constructor)))
        self.driver.find_element(By.XPATH, mylocators.constructor).click()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.burger_ingredients)))
        assert self.driver.find_element(By.XPATH, mylocators.burger_ingredients)
        self.driver.quit()

    def test_constructor_from_logo(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.login()
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.logo)))
        self.driver.find_element(By.XPATH, mylocators.logo).click()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.burger_ingredients)))
        assert self.driver.find_element(By.XPATH, mylocators.burger_ingredients)
        self.driver.quit()
