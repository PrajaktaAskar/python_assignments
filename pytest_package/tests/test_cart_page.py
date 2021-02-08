from pytest_package.pages.add_to_cart_page import AddToCart
from pytest_package.pages.cart_page import Cart
import logging
from pytest_package.utilities import custome_logger as cl
import pytest


class TestCart:
    log = cl.customLogger(logging.DEBUG)
    test_data_zip_codes = [("chair", "ABC12"),("sofa", "XYZ123")]

    @pytest.mark.parametrize("product_name, coupon", test_data_zip_codes)
    def test_chair_cart(self, setup, product_name, coupon):
        at_cart = AddToCart(setup)
        cart = Cart(setup)
        at_cart.add_to_cart_product(product_name)
        cart.enter_coupon_code(coupon)
        self.log.info("Coupon entered successfully")
        cart.click_apply_coupon()
        self.log.info("Testcase passed")