import logging
import allure

from pom.locators.login_page_locators import LoginPageLocators
from pom.page.abs_base_page import AbsBasePage


class LoginPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="")
        self.logger = logging.getLogger("LoginPage")

    
    @allure.step("Проверка видимости кнопки 'Регистрация'")
    def displayed_reg_btn(self):
        return self._is_element_visible(LoginPageLocators.REGISTRATION_BTN)

    @allure.step("Получение заголовка страницы входа")
    def title_login_page(self) -> str:
        return self.wait_visible(LoginPageLocators.TITLE_LOGIN_PAGE).text

    @allure.step("Переход на страницу регистрации")
    def click_registration(self):
        from pom.page.registration_page import RegistrationPage

        self._click(LoginPageLocators.REGISTRATION_BTN)
        return RegistrationPage(self._driver, self._base_url)

    @allure.step("Проверка видимости заголовка страницы входа")
    def displayed_title_login_page(self):
        return self._is_element_visible(LoginPageLocators.TITLE_LOGIN_PAGE)

    @allure.step("Проверка видимости формы входа")
    def displayed_login_form(self):
        return self._is_element_visible(LoginPageLocators.LOGIN_FORM)

    @allure.step("Проверка видимости кнопки 'Войти' (Submit)")
    def displayed_btn_submit(self):
        return self._is_element_visible(LoginPageLocators.BTN_SUBMIT)

    @allure.step("Проверка нахождения на странице входа (по URL)")
    def _is_login_url(self) -> bool:
        current_url = self._driver.current_url
        if "login?" in current_url:
            return True
        else:
            return False
