from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import mylocators


class TestLoginToStellarBurgers:

    def start(self):
        self.email = 'julia_panfilova_02@yandex.ru'
        self.password = '123456'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def login(self):
        self.driver.find_element(By.XPATH, mylocators.email).send_keys(self.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(self.password)
        self.driver.find_element(By.XPATH, mylocators.enter).click()

    def test_login_by_button_entry(self):
        self.start()
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(By.XPATH, mylocators.enter_account).click()
        self.login()
        WebDriverWait(self.driver, 15)
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()

    def test_login_by_button_personal_account(self):
        self.start()
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        self.login()
        WebDriverWait(self.driver, 10)
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()

    def test_login_by_button_in_registration_form(self):
        self.start()
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, mylocators.enter_from_registration).click()
        self.login()
        WebDriverWait(self.driver, 10)
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()

    def test_login_by_button_restore_password(self):
        self.start()
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        self.driver.find_element(By.XPATH, mylocators.enter_from_restore_password).click()
        self.login()
        WebDriverWait(self.driver, 10)
        assert self.driver.find_element(By.XPATH, mylocators.order)
        self.driver.quit()