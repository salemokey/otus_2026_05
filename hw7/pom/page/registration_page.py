from selenium.webdriver.support import expected_conditions as EC

from pom.locators.registration_page_locators import RegistrationPageLocators
from pom.page.abs_base_page import AbsBasePage
from pom.page.login_page import LoginPage


class RegistrationPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")

    def open(self):
        login_page = LoginPage(self._driver, self._base_url)
        login_page.open()
        login_page.click_registration()

    def displayed_title_registration_page(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.TITLE_RERISTRATION_PAGE
            )
        )
        return element

    def displayed_gender_btn(self):
        element = self.wait.until(
            EC.presence_of_all_elements_located(RegistrationPageLocators.GENDER_BTN)
        )
        return len(element)

    def displayed_firstname(self):
        element = self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.FIRSTNAME)
        )
        return element

    def displayed_lastname(self):
        element = self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.LASTNAME)
        )
        return element

    def displayed_email(self):
        element = self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL)
        )
        return element

    def displayed_password(self):
        element = self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD)
        )
        return element

    def displayed_birthday(self):
        element = self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.BIRTHDAY)
        )
        return element

    def click_save_btn(self):
        element = self.wait.until(
            EC.visibility_of_element_located(RegistrationPageLocators.SAVE_BTN)
        )
        element.click()
        return element

    def click_gender_btn(self, gender):
        by, locator_template = RegistrationPageLocators.GENDER_BTN_TEMPLATE
        new_locator = locator_template.format(gender)
        ready_locator = (by, new_locator)
        element = self.wait.until(EC.element_to_be_clickable(ready_locator))
        element.click()
        return element

    def click_all_checkboxes(self):
        for i in RegistrationPageLocators.ALL_CHECKBOXES:
            element = self.wait.until(EC.element_to_be_clickable(i))
            element.click()
