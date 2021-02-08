from pytest_package.pages.product_info_page import ProductInfoPage
from selenium.webdriver.common.by import By
#used pytest HTML plugin "--html=reports\report.html" in terminal
from pytest_package.utilities import custome_logger as cl
import logging


class TestProduct:

    log = cl.customLogger(logging.DEBUG)

    def test_product1(self, setup):
        prod_info = ProductInfoPage(setup)
        prod_info.click_product()
        prod_info.click_study_table()
        prod_info.click_product1()

        product_name = setup.find_element(By.XPATH,"//h1[@class='product_title entry-title']").text
        self.log.info("Product name is: " + product_name)
        assert product_name == "CORNER STUDY TABLE WITH CHAIR"
