from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from assignment2_unit.base.locators import Locators


class OverViewProduct():

    def __init__(self, driver):
        self.driver = driver

    def click_product_link(self):
        self.driver.find_element(By.LINK_TEXT,Locators._product_linkText).click()

    def click_quick_view(self):
        self.driver.find_element(By.CLASS_NAME,Locators._quick_view_className).click()
        time.sleep(5)

    def close_quick_view(self):
        self.driver.find_element(By.ID,Locators._close_quickView_id).click()



