from selenium.webdriver.common.by import By
from selenium import webdriver
import re
import mylocators
import myconsts


class TestRegistrationToStellarBurgers:
    def setup_class(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, mylocators.username).send_keys(myconsts.name)
        self.driver.find_element(By.XPATH, mylocators.email_register).send_keys(myconsts.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(myconsts.password)
        self.driver.implicitly_wait(30)

    def test_name_not_blank(self):
        assert len(myconsts.name) != 0, "Name is blank"

    def test_email_with_valid_format(self):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        assert re.fullmatch(regex, myconsts.email), 'The email format is invalid'

    def test_password_at_least_6_characters(self):
        assert len(myconsts.password) > 5, "Password is less than 6 characters"

    def test_password_invalid(self):
        if len(myconsts.password) < 6:
            assert self.driver.find_element(By.XPATH, mylocators.incorrect_password)

    def test_success_registration(self):
        self.driver.find_element(By.XPATH, mylocators.register).click()
        if self.driver.find_element(By.XPATH, mylocators.user_already_exists) is None:
            assert self.driver.find_element(By.XPATH, mylocators.enter)
        else:
            print('The user already exists')
            self.driver.quit()