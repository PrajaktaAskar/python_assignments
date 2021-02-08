from selenium.webdriver.common.by import By
from pytest_package.base.locators import Locators


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def enter_coupon_code(self,coupon):
        self.driver.find_element(By.ID, Locators._coupon_code_id).send_keys(coupon)

    def click_apply_coupon(self):
        self.driver.find_element(By.NAME, Locators._apply_coupon_button_name).click()