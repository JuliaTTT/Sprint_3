from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import mylocators


class TestConstructor:
    def start(self):
        self.email = 'julia_panfilova_02@yandex.ru'
        self.password = '123456'
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.implicitly_wait(5)

    def login(self):
        self.driver.find_element(By.XPATH, mylocators.email).send_keys(self.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(self.password)
        self.driver.find_element(By.XPATH, mylocators.enter).click()

    def test_constructor_from_personal_account(self):
        self.start()
        self.login()
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, mylocators.constructor).click()
        WebDriverWait(self.driver, 10)
        assert self.driver.find_element(By.XPATH, mylocators.burger_ingredients)
        self.driver.quit()

    def test_constructor_from_logo(self):
        self.start()
        self.login()
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, mylocators.logo).click()
        WebDriverWait(self.driver, 10)
        assert self.driver.find_element(By.XPATH, mylocators.burger_ingredients)
        self.driver.quit()
