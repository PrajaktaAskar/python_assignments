class Locators:
    # Locators welcome page
    _home_link_text = "Home"
    _product_link_text = "Products"
    _about_us_xpath = "//li[@id='menu-item-299']//a[text()='About Us']"

    #locators product categories
    _study_table_xpath = "//li[@class='cat-item cat-item-28']"
    _product1_xpath = "//h2[contains(text(),'Corner Study Table with Chair')]"
    _product2_xpath = "//ul[@class='products columns-3']//following-sibling::li[2]"

    @property
    def home_link_text(self):
        return self._home_link_text

    @property
    def study_table_xpath(self):
        return self._study_table_xpath

    @property
    def product2_xpath(self):
        return self._product2_xpath

    @property
    def product1_xpath(self):
        return self._product1_xpath

    @property
    def product_link_text(self):
        return self._product_link_text

    #search page

    _searchbox_id = "woocommerce-product-search-field-0"
    _search_button_xpath = "//button[contains(text(),'Search')]"
    _select_product_chair_xpath = "//h2[@class='woocommerce-loop-product__title']"
    _select_product_sofa_xpath = "//h2[@class='woocommerce-loop-product__title']"
    _add_to_cart_name = "add-to-cart"
    _view_cartButton_xpath = "//a[@class='added_to_cart wc-forward']"

    #cart page
    _coupon_code_id = 'coupon_code'
    _apply_coupon_button_name = 'apply_coupon'