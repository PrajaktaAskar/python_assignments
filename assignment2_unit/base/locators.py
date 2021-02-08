class Locators():

    # Over view page
    _product_linkText = "Products"
    _quick_view_className = "ast-quick-view-text"
    _close_quickView_id = "ast-quick-view-close"

    # add to cart page

    #_product_linkText = "Products"
    _search_box_id = "woocommerce-product-search-field-0"
    _search_button_xpath = "//button[contains(text(),'Search')]"
    _select_product_xpath = "//h2[@class='woocommerce-loop-product__title']"
    _add_to_cart_name = "add-to-cart"
    _view_cartButton_xpath = "//a[@class='added_to_cart wc-forward']"
