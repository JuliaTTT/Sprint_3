import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import mylocators


@pytest.mark.usefixtures("start_for_constructor")
class TestBurgerIngredientSection:

    def test_go_to_rolls(self):
        self.driver.find_element(By.XPATH, mylocators.fillings).click()
        WebDriverWait(self.driver, 30).until(visibility_of_element_located((By.XPATH, mylocators.rolls_header)))
        self.driver.find_element(By.XPATH, mylocators.rolls).click()
        assert self.driver.find_element(By.XPATH, mylocators.rolls_header)
        self.driver.quit()

    def test_go_to_sauces(self):
        self.driver.find_element(By.XPATH, mylocators.sauces).click()
        WebDriverWait(self.driver, 30).until(visibility_of_element_located((By.XPATH, mylocators.sauces_border)))
        assert self.driver.find_element(By.XPATH, mylocators.sauces_border).value_of_css_property('box-shadow').__contains__('rgb(47, 47, 55)') == 1
        self.driver.quit()

    def test_go_to_fillings(self):
        self.driver.find_element(By.XPATH, mylocators.fillings).click()
        WebDriverWait(self.driver, 30).until(visibility_of_element_located((By.XPATH, mylocators.fillings_border)))
        assert self.driver.find_element(By.XPATH, mylocators.fillings_border).value_of_css_property('box-shadow').__contains__('rgb(47, 47, 55)') == 1
        self.driver.quit()
