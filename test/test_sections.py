from selenium.webdriver.common.by import By
from selenium import webdriver
import mylocators


class TestBurgerIngredientSection:

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, mylocators.constructor).click()

    def test_go_to_rolls(self):
        self.start()
        self.driver.find_element(By.XPATH, mylocators.fillings).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH, mylocators.rolls).click()
        assert self.driver.find_element(By.XPATH, mylocators.rolls_header)
        self.driver.quit()

    def test_go_to_sauces(self):
        self.start()
        self.driver.find_element(By.XPATH, mylocators.sauces).click()
        self.driver.implicitly_wait(15)
        assert self.driver.find_element(By.XPATH, mylocators.sauces_border).value_of_css_property('box-shadow').__contains__('rgb(47, 47, 55)') == 1
        self.driver.quit()

    def test_go_to_fillings(self):
        self.start()
        self.driver.find_element(By.XPATH, mylocators.fillings).click()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.XPATH, mylocators.fillings_border).value_of_css_property('box-shadow').__contains__('rgb(47, 47, 55)') == 1
        self.driver.quit()
