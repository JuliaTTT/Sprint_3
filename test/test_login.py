import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import mylocators
import myconsts


@pytest.mark.usefixtures("start_for_login")
class TestLoginToStellarBurgers:

    def login(self):
        self.driver.find_element(By.XPATH, mylocators.email).send_keys(myconsts.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(myconsts.password)
        self.driver.find_element(By.XPATH, mylocators.enter).click()

    def test_login_by_button_entry(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(By.XPATH, mylocators.enter_account).click()
        self.login()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.order)))
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()

    def test_login_by_button_personal_account(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        self.login()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.order)))
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()

    def test_login_by_button_in_registration_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, mylocators.enter_from_registration).click()
        self.login()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.order)))
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()

    def test_login_by_button_restore_password(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        self.driver.find_element(By.XPATH, mylocators.enter_from_restore_password).click()
        self.login()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.order)))
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()