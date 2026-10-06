import logging

import allure

from pom.components.header import HeaderComponent
from pom.locators.main_page_locators import MainPageLocators
from pom.page.abs_base_page import AbsBasePage


class MainPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, "/")
        self.header = HeaderComponent(browser, base_url, "")
        self.logger = logging.getLogger("MainPage")

    @allure.step("Проверка видимости заголовка страницы")
    def displayed_title(self):
        return self._is_element_visible(MainPageLocators.HEADER_ELEMENT)

    @allure.step("Проверка видимости карусели товаров")
    def displayed_carousel(self):
        return self._is_element_visible(MainPageLocators.CAROUSEL_ELEMENT)

    @allure.step("Проверка видимости информации о пользователе")
    def displayed_user_info(self) -> bool:
        return self.header.displayed_user_info()

    @allure.step("Проверка видимости блока 'Популярные товары'")
    def displayed_popular_title(self):
        return self._is_element_visible(MainPageLocators.POPULAR_TITLE)

    @allure.step("Проверка видимости списка продуктов")
    def displayed_products(self):
        return self._is_element_visible(MainPageLocators.PRODUCTS_ROW)

    @allure.step("Переход на страницу товара (клик по первому товару)")
    def click_on_product(self):
        from pom.page.product_page import ProductPage

        self._click(MainPageLocators.PRODUCT_TITLE)
        return ProductPage(self._driver, self._base_url)

    @allure.step("Переход на страницу авторизации")
    def click_on_login(self):
        from pom.page.login_page import LoginPage

        self._click(MainPageLocators.LOGIN_BTN)
        return LoginPage(self._driver, self._base_url)

    @allure.step("Проверка текущей валюты")
    def displayed_currency(self):
        return self._is_element_visible(MainPageLocators.CURRENT_PRICE)

    @allure.step("Проверка доступности меню выбора валюты")
    def dropdown_currency(self):
        return self._is_element_visible(MainPageLocators.DROPDOWN_CURRENCY)

    @allure.step("Смена валюты на USD")
    def change_currency_to_usd(self):
        return self.header.change_currency_to_usd()

    @allure.step("Получение актуальной цены товара")
    def get_updated_price(self) -> str:
        element = self.wait_visible(MainPageLocators.UPDATED_PRICE)
        return element.text
