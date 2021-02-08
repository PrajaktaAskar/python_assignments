from selenium import webdriver
from selenium.webdriver.common.by import By
from assignment2_unit.base.locators import Locators

class AddToCart():
    def __init__(self,driver):
        self.driver= driver

    #Locators

    def click_product_link(self):
        self.driver.find_element(By.LINK_TEXT, Locators._product_linkText).click()

    def click_search_box(self,product_name):
        self.driver.find_element(By.ID, Locators._search_box_id).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,Locators._search_button_xpath).click()

    def click_on_product(self):
        self.driver.find_element(By.XPATH,Locators._select_product_xpath).click()

    def click_add_to_cart(self):
        self.driver.find_element(By.NAME,Locators._add_to_cart_name).click()

    def click_view_cart_button(self):
         self.driver.find_element(By.XPATH,Locators._view_cartButton_xpath).click()
