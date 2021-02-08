from selenium import webdriver
from assignment2_unit.page.add_cart import AddToCart
import unittest


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://letskodeit.com/automationpractice/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_add_to_cart(self):
        driver = self.driver
        add_to = AddToCart(driver)
        add_to.click_product_link()
        add_to.click_search_box(product_name="chair")
        add_to.click_search_button()
        add_to.click_on_product()
        add_to.click_add_to_cart()
        add_to.click_view_cart_button()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")
