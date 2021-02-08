from selenium import webdriver
from assignment2_unit.page.over_view import OverViewProduct
import unittest


class OverviewTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://letskodeit.com/automationpractice/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_over_view(self):
        driver = self.driver
        ov = OverViewProduct(driver)  # empty it
        ov.click_product_link()
        ov.click_quick_view()
        ov.close_quick_view()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
