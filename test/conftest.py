import pytest
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import mylocators
from selenium.webdriver.common.by import By


@pytest.fixture()
def start_for_login(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.implicitly_wait(15)


@pytest.fixture()
def start_for_constructor(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(request.cls.driver, 15).until(visibility_of_element_located((By.XPATH, mylocators.constructor)))
    request.cls.driver.find_element(By.XPATH, mylocators.constructor).click()



