from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import mylocators


class TestPersonalAccount:
    def start(self):
        self.email = 'julia_panfilova_02@yandex.ru'
        self.password = '123456'
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.implicitly_wait(5)

    def login(self):
        self.driver.find_element(By.XPATH, mylocators.username).send_keys(self.email)
        self.driver.find_element(By.XPATH, mylocators.password).send_keys(self.password)
        self.driver.find_element(By.XPATH, mylocators.enter).click()

    def test_go_to_personal_account(self):
        self.start()
        self.login()
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 10)
        assert self.driver.find_element(By.XPATH, "//a[@href='/account/profile']")
        self.driver.quit()

