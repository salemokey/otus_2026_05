from pom.components.header import HeaderComponent
from pom.locators.main_page_locators import MainPageLocators
from pom.page.abs_base_page import AbsBasePage


class MainPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, "/")
        self.header = HeaderComponent(browser, base_url, "")

    def displayed_title(self):
        return self._is_element_visible(MainPageLocators.HEADER_ELEMENT)

    def displayed_carousel(self):
        return self._is_element_visible(MainPageLocators.CAROUSEL_ELEMENT)

    def displayed_user_info(self):
        return self._is_element_visible(MainPageLocators.USER_INFO_ELEMENT)

    def displayed_popular_title(self):
        return self._is_element_visible(MainPageLocators.POPULAR_TITLE)

    def displayed_products(self):
        return self._is_element_visible(MainPageLocators.PRODUCTS_ROW)

    def click_on_product(self):
        from pom.page.product_page import ProductPage

        self._click(MainPageLocators.PRODUCT_TITLE)
        return ProductPage(self._driver, self._base_url)

    def click_on_login(self):
        from pom.page.login_page import LoginPage

        self._click(MainPageLocators.LOGIN_BTN)
        return LoginPage(self._driver, self._base_url)

    def displayed_currency(self):
        return self._is_element_visible(MainPageLocators.CURRENT_PRICE)

    def dropdown_currency(self):
        return self._is_element_visible(MainPageLocators.DROPDOWN_CURRENCY)

    def change_currency_to_usd(self):
        return self.header.change_currency_to_usd()

    def get_updated_price(self) -> str:
        element = self.wait_visible(MainPageLocators.UPDATED_PRICE)
        return element.text
