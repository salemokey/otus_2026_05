from pom.locators.product_page_locators import ProductPageLocators
from pom.page.abs_base_page import AbsBasePage


class ProductPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")

    def displayed_product_name(self):
        return self._is_element_visible(ProductPageLocators.PRODUCT_NAME)

    def displayed_add_to_cart_btn(self):
        return self._is_element_visible(ProductPageLocators.ADD_TO_CART_BUTTON)

    def displayed_description(self):
        return self._is_element_visible(ProductPageLocators.PRODUCT_DESCRIPTION)

    def displayed_comments(self):
        return self._is_element_visible(ProductPageLocators.COMMENTS_LIST)

    def displayed_wish_btn(self):
        return self._is_element_visible(ProductPageLocators.WISH_BTN)

    def open_cart_from_modal(self):
        from pom.page.cart_page import CartPage

        self._click(ProductPageLocators.ADD_TO_CART_BUTTON)
        self._click(ProductPageLocators.CONTINUE_CART_BTN)

        return CartPage(self._driver, self._base_url)
