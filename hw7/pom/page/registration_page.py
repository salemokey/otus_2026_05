from selenium.webdriver.support import expected_conditions as EC

from pom.locators.registration_page_locators import RegistrationPageLocators
from pom.page.abs_base_page import AbsBasePage


class RegistrationPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/registration")

    def displayed_title_registration_page(self):
        return self._is_element_visible(
            RegistrationPageLocators.TITLE_RERISTRATION_PAGE
        )

    def title_registration_page(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.TITLE_RERISTRATION_PAGE
            )
        )
        return element.text

    def displayed_gender_btn(self):
        element = self.wait.until(
            EC.presence_of_all_elements_located(RegistrationPageLocators.GENDER_BTN)
        )
        return len(element)

    def displayed_firstname(self):
        return self._is_element_visible(RegistrationPageLocators.FIRSTNAME)

    def displayed_lastname(self):
        return self._is_element_visible(RegistrationPageLocators.LASTNAME)

    def displayed_email(self):
        return self._is_element_visible(RegistrationPageLocators.EMAIL)

    def displayed_password(self):
        return self._is_element_visible(RegistrationPageLocators.PASSWORD)

    def displayed_birthday(self):
        return self._is_element_visible(RegistrationPageLocators.BIRTHDAY)

    def click_save_btn(self):
        self._click(RegistrationPageLocators.SAVE_BTN)

    def click_gender_btn(self, gender):
        by, locator_template = RegistrationPageLocators.GENDER_BTN_TEMPLATE
        new_locator = locator_template.format(gender)
        ready_locator = (by, new_locator)
        self._click(ready_locator)

    def click_all_checkboxes(self):
        for i in RegistrationPageLocators.ALL_CHECKBOXES:
            self._click(i)

    def input_values(self):
        self._input_text("test", RegistrationPageLocators.FIRSTNAME)
        self._input_text("testering", RegistrationPageLocators.LASTNAME)
        self._input_text("test@1231.com", RegistrationPageLocators.EMAIL)
        self._input_text("NewPassword123!", RegistrationPageLocators.PASSWORD)
        self._input_text("03/07/2007", RegistrationPageLocators.BIRTHDAY)
