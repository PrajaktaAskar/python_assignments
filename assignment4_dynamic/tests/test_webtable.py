import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assignment4_dynamic.page.webtable_page import WebTable

test_url = "https://www.w3schools.com/html/html_tables.asp"


class WebTableTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(test_url)
        self.web = WebTable(self.driver)

    def test_1_get_num_rows(self):
        self.web.get_num_rows()

    def test_2_get_num_col(self):
        self.web.get_num_col()

    def test_3_get_all_data(self):
        self.web.get_all_data()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
