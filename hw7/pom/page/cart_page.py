import logging
import allure

from pom.components.header import HeaderComponent
from pom.locators.cart_page_locators import CartPageLocators
from pom.page.abs_base_page import AbsBasePage


class CartPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")
        self.header = HeaderComponent(browser, base_url, "")
        self.logger = logging.getLogger("CartPage")

    @allure.step("Проверка наличия добавленного товара в корзине")
    def added_product_is_displayed(self):
        return self._is_element_visible(CartPageLocators.ADDED_PRODUCT)

    @allure.step("Получение размера скидки")
    def product_discount(self):
        element = self.wait_visible(CartPageLocators.PRODUCT_DISCOUNT).text
        return element

    @allure.step("Получение базовой цены товара")
    def price(self):
        element = self.wait_visible(CartPageLocators.PRICE).text
        return element

    @allure.step("Получение итоговой цены позиции в корзине")
    def product_price(self):
        element = self.wait_visible(CartPageLocators.PRODUCT_PRICE).text
        return element

    @allure.step("Получение промежуточного итога (Subtotal)")
    def subtotal(self):
        element = self.wait_visible(CartPageLocators.SUBTOTAL).text
        return element

    @allure.step("Получение стоимости доставки (Shipping)")
    def shipping(self):
        element = self.wait_visible(CartPageLocators.SHIPPING).text
        return element

    @allure.step("Получение общей суммы заказа (Total)")
    def total(self):
        element = self.wait_visible(CartPageLocators.TOTAL).text
        return element

    @allure.step("Удаление товара из корзины")
    def remove_product(self):
        self._click(CartPageLocators.REMOVE_BTN)

    @allure.step("Подсчет количества товаров в корзине")
    def count_cart_items(self):
        element = self.wait_visible_all(CartPageLocators.CART_ITEMS)
        return len(element)

    @allure.step("Проверка сообщения 'Корзина пуста'")
    def no_items_title(self):
        return self._is_element_visible(CartPageLocators.NO_ITEMS_TITLE)

    @allure.step("Смена валюты на странице корзины")
    def change_currency_cart_page(self):
        return self.header.change_currency_to_usd()
