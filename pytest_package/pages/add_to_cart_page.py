from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_package.base.locators import Locators

class AddToCart:
    def __init__(self,driver):
        self.driver = driver

    #Locators

    def click_product_link(self):
        self.driver.find_element(By.LINK_TEXT,Locators._product_link_text).click()

    def click_search_box(self, product_name):
        self.driver.find_element(By.ID, Locators._searchbox_id).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,Locators._search_button_xpath).click()
    #productname given chair

    def click_on_product1(self):
        self.driver.find_element(By.XPATH,Locators._select_product_chair_xpath).click()

    def click_on_product2(self):
        self.driver.find_element(By.XPATH,Locators._select_product_sofa_xpath).click()

    def click_add_to_cart(self):
        self.driver.find_element(By.NAME,Locators._add_to_cart_name).click()

    def click_view_cart_button(self):
         self.driver.find_element(By.XPATH,Locators._view_cartButton_xpath).click()

    def add_to_cart_product(self, product_name):
        self.click_product_link()
        self.click_search_box(product_name)
        self.click_search_button()
        self.click_on_product1()
        self.click_add_to_cart()
        self.click_view_cart_button()

    # def add_to_cart_sofa(self, product_name):
    #     self.click_product_link()
    #     self.click_search_box(product_name)
    #     self.click_search_button()
    #     self.click_on_product2()
    #     self.click_add_to_cart()
    #     self.click_view_cart_button()