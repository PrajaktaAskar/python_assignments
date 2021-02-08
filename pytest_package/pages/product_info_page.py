from selenium.webdriver.common.by import By
from pytest_package.base.locators import Locators
import time


class ProductInfoPage():

    def __init__(self, driver):
        self.driver = driver

    # locators
    # locators product categories
    _product_link_text = "Products"
    _study_table_xpath = "//li[@class='cat-item cat-item-28']//a[text()='Study table']"
    _product1_xpath = "//h2[contains(text(),'Corner Study Table with Chair')]"
    _product2_xpath = "//ul[@class='products columns-3']//following-sibling::li[2]"

    def click_product(self):
        self.driver.find_element(By.LINK_TEXT, self._product_link_text).click()

    def click_study_table(self):
        self.driver.find_element(By.XPATH, self._study_table_xpath).click()
        time.sleep(5)

    def click_product1(self):
        self.driver.find_element(By.XPATH, self._product1_xpath).click()
        time.sleep(3)

    def click_product2(self):
        self.driver.find_element(By.XPATH, self._product2_xpath).click()
