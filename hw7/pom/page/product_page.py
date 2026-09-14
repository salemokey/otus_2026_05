from selenium.webdriver.support import expected_conditions as EC

from pom.locators.product_page_locators import ProductPageLocators
from pom.page.abs_base_page import AbsBasePage
from pom.page.main_page import MainPage


class ProductPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")

    def open(self):
        main_page = MainPage(self._driver, self._base_url)
        main_page.open()
        product_title_from_main = main_page.click_on_product()
        return product_title_from_main

    def displayed_product_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME)
        )
        return element

    def displayed_add_to_cart_btn(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.ADD_TO_CART_BUTTON)
        )
        return element

    def displayed_description(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_DESCRIPTION)
        )
        return element

    def displayed_comments(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.COMMENTS_LIST)
        )
        return element

    def displayed_wish_btn(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.WISH_BTN)
        )
        return element

    def open_cart_from_modal(self):
        element = self.wait.until(
            EC.element_to_be_clickable(ProductPageLocators.CONTINUE_CART_BTN)
        )
        element.click()
