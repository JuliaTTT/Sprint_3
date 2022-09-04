from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import mylocators


class TestExitFromAccount:
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
        self.driver.find_element(By.XPATH, mylocators.personal_account).click()
        WebDriverWait(self.driver, 10)

    def test_exit_from_personal_account(self):
        self.start()
        self.login()
        self.driver.find_element(By.XPATH, mylocators.exit).click()
        WebDriverWait(self.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.enter)))
        assert self.driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        self.driver.quit()
