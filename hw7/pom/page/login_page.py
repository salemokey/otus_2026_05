from selenium.webdriver.support import expected_conditions as EC

from pom.locators.login_page_locators import LoginPageLocators
from pom.page.abs_base_page import AbsBasePage


class LoginPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")

    def displayed_reg_btn(self):
        return self._is_element_visible(LoginPageLocators.REGISTRATION_BTN)

    def title_login_page(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.TITLE_LOGIN_PAGE)
        ).text

    def click_registration(self):
        from pom.page.registration_page import RegistrationPage

        self._click(LoginPageLocators.REGISTRATION_BTN)
        return RegistrationPage(self._driver, self._base_url)

    def displayed_title_login_page(self):
        return self._is_element_visible(LoginPageLocators.TITLE_LOGIN_PAGE)

    def displayed_login_form(self):
        return self._is_element_visible(LoginPageLocators.LOGIN_FORM)

    def displayed_btn_submit(self):
        return self._is_element_visible(LoginPageLocators.BTN_SUBMIT)

    def _is_login_url(self) -> bool:
        current_url = self._driver.current_url
        if "login?" in current_url:
            return True
        else:
            return False
