from selenium.webdriver.support import expected_conditions as EC

from pom.locators.login_page_locators import LoginPageLocators
from pom.page.abs_base_page import AbsBasePage
from pom.page.main_page import MainPage


class LoginPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")

    def open(self):
        main_page = MainPage(self._driver, self._base_url)
        main_page.open()
        main_page.click_on_login()

    def click_registration(self):
        element = self.wait.until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTRATION_BTN)
        )
        element.click()

    def displayed_title_login_page(self):
        element = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.TITLE_LOGIN_PAGE)
        )
        return element

    def displayed_login_form(self):
        element = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)
        )
        return element

    def displayed_btn_submit(self):
        element = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.BTN_SUBMIT)
        )
        return element
