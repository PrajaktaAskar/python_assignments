from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WelcomePage:

    def __init__(self, driver):
        self.driver = driver

    #Locators
    _home_link_text = "Home"
    _product_link_text = "Products"
    _about_us_xpath = "//li[@id='menu-item-299']//a[text()='About Us']"

    def get_title(self):
        page_title = self.driver.title
        print("Page Title is:" + page_title)

    def click_home(self):
        self.driver.find_element(By.LINK_TEXT, self._home_link_text).click()
        self.driver.back()
        time.sleep(2)

    def click_product(self):
        self.driver.find_element(By.LINK_TEXT, self._product_link_text).click()
        self.driver.back()
        time.sleep(5)

    def click_about_us(self):
        self.driver.find_element(By.XPATH, self._about_us_xpath).click()
        text_button = self.driver.find_element(By.XPATH, "//span[@class='elementor-button-text']").text
        print(text_button)
        self.driver.back()

    def checkWelcomeLinks(self):
        self.click_product()
        self.click_about_us()