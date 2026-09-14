from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pom.locators.main_page_locators import MainPageLocators


class AbsBasePage(ABC):
    _driver: WebDriver

    def __init__(self, browser, base_url, path: str):
        self._driver = browser
        self._base_url = base_url
        self._path = path
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self._driver.get(self._base_url + self._path)

    def change_currency_to_usd(self):
        self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.CURRENT_PRICE))
        )

        self.wait.until(
            EC.visibility_of_element_located((MainPageLocators.DROPDOWN_CURRENCY))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((MainPageLocators.DROPDOWN_OPTION))
        ).click()

        self.wait.until(
            EC.text_to_be_present_in_element(
                MainPageLocators.DROPDOWN_OPTION_DOLLARS["locator"],
                MainPageLocators.DROPDOWN_OPTION_DOLLARS["text"],
            )
        )

        self.wait.until(EC.url_contains("id_currency=2"))

        return self
