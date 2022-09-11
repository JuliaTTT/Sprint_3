import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import mylocators
import myconsts


@pytest.mark.usefixtures("start_for_login")
class TestPersonalAccount:
    def login(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, mylocators.username).send_keys(myconsts.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(myconsts.password)
        self.driver.find_element(By.XPATH, mylocators.enter).click()

    def test_go_to_personal_account(self):
        self.login()
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 30).until(visibility_of_element_located((By.XPATH, mylocators.personal_account_profile)))
        assert self.driver.find_element(By.XPATH, mylocators.personal_account_profile)
        self.driver.quit()

