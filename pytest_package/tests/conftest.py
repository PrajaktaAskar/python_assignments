from selenium import webdriver
import pytest


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://letskodeit.com/automationpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()
