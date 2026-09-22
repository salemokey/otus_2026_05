from pom.components.header import HeaderComponent
from pom.locators.cart_page_locators import CartPageLocators
from pom.page.abs_base_page import AbsBasePage


class CartPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")
        self.header = HeaderComponent(browser, base_url, "")

    def added_product_is_displayed(self):
        self._is_element_visible(CartPageLocators.ADDED_PRODUCT)

    def product_discount(self):
        element = self.wait_visible(CartPageLocators.PRODUCT_DISCOUNT).text
        return element

    def price(self):
        element = self.wait_visible(CartPageLocators.PRICE).text
        return element

    def product_price(self):
        element = self.wait_visible(CartPageLocators.PRODUCT_PRICE).text
        return element

    def subtotal(self):
        element = self.wait_visible(CartPageLocators.SUBTOTAL).text
        return element

    def shipping(self):
        element = self.wait_visible(CartPageLocators.SHIPPING).text
        return element

    def total(self):
        element = self.wait_visible(CartPageLocators.TOTAL).text
        return element

    def remove_product(self):
        return self._click(CartPageLocators.REMOVE_BTN)

    def count_cart_items(self):
        element = self.wait_visible_all(CartPageLocators.CART_ITEMS)
        return len(element)

    def no_items_title(self):
        return self._is_element_visible(CartPageLocators.NO_ITEMS_TITLE)

    def change_currency_cart_page(self):
        return self.header.change_currency_to_usd()
