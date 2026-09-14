from selenium.webdriver.support import expected_conditions as EC

from pom.locators.cart_page_locators import CartPageLocators
from pom.page.abs_base_page import AbsBasePage
from pom.page.product_page import ProductPage


class CartPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")

    def open_from_modal(self):
        product_page = ProductPage(self._driver, self._base_url)
        product_page.open()
        add_to_cart_btn = product_page.displayed_add_to_cart_btn()
        add_to_cart_btn.click()
        product_page.open_cart_from_modal()
        self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.ADDED_PRODUCT)
        )

    def product_discount(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.PRODUCT_DISCOUNT)
        ).text
        return element

    def price(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.PRICE)
        ).text
        return element

    def product_price(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.PRODUCT_PRICE)
        ).text
        return element

    def subtotal(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.SUBTOTAL)
        ).text
        return element

    def shipping(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.SHIPPING)
        ).text
        return element

    def total(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.TOTAL)
        ).text
        return element

    def remove_product(self):
        element = self.wait.until(
            EC.element_to_be_clickable(CartPageLocators.REMOVE_BTN)
        )
        element.click()
        return element

    def count_cart_items(self):
        element = self.wait.until(
            EC.visibility_of_all_elements_located(CartPageLocators.CART_ITEMS)
        )
        return len(element)

    def no_items_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CartPageLocators.NO_ITEMS_TITLE)
        )
        return element
