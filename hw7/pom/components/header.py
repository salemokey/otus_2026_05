from selenium.webdriver.support import expected_conditions as EC

from pom.locators.main_page_locators import MainPageLocators
from pom.page.abs_base_page import AbsBasePage


class HeaderComponent(AbsBasePage):
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
