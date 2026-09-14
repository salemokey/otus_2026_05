from selenium.webdriver.support import expected_conditions as EC

from pom.locators.main_page_locators import MainPageLocators
from pom.page.abs_base_page import AbsBasePage


class MainPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, "/")

    def displayed_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.HEADER_ELEMENT))
        )
        return element

    def displayed_carousel(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.CAROUSEL_ELEMENT))
        )
        return element

    def displayed_user_info(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.USER_INFO_ELEMENT))
        )
        return element

    def displayed_popular_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.POPULAR_TITLE))
        )
        return element

    def displayed_products(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.PRODUCTS_ROW))
        )
        return element

    def click_on_product(self):
        product_element = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.PRODUCT_TITLE)
        )
        product_element_title = product_element.text.upper()
        product_element.click()
        return product_element_title

    def click_on_login(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BTN)
        )
        login_btn.click()
        return login_btn

    def displayed_currency(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.CURRENT_PRICE))
        )
        return element

    def dropdown_currency(self):
        element = self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.DROPDOWN_CURRENCY))
        )
        return element

    def dropdown_option(self, currency):
        if "€" in currency:
            element = self.wait.until(
                EC.element_to_be_clickable((MainPageLocators.DROPDOWN_OPTION))
            )
            return element
        else:
            return None

    def wait_new_currency(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                MainPageLocators.DROPDOWN_OPTION_DOLLARS["locator"],
                MainPageLocators.DROPDOWN_OPTION_DOLLARS["text"],
            )
        )

    def updated_price(self):
        element = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.UPDATED_PRICE)
        ).text
        return element

    def wait_currency_url(self):
        self.wait.until(EC.url_contains("id_currency=2"))
