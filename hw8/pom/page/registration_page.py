import logging

import allure
from selenium.webdriver.support import expected_conditions as EC

from pom.locators.registration_page_locators import RegistrationPageLocators
from pom.page.abs_base_page import AbsBasePage


class RegistrationPage(AbsBasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/registration")
        self.logger = logging.getLogger("RegistrationPage")

    @allure.step("Проверка видимости заголовка страницы регистрации")
    def displayed_title_registration_page(self):
        return self._is_element_visible(
            RegistrationPageLocators.TITLE_RERISTRATION_PAGE
        )

    @allure.step("Получение текста заголовка страницы регистрации")
    def title_registration_page(self) -> str:
        element = self.wait_visible(RegistrationPageLocators.TITLE_RERISTRATION_PAGE)
        return element.text

    @allure.step("Проверка наличия кнопок выбора пола")
    def displayed_gender_btn(self):
        element = self.wait.until(
            EC.presence_of_all_elements_located(RegistrationPageLocators.GENDER_BTN)
        )
        return len(element)

    @allure.step("Проверка видимости поля 'Имя'")
    def displayed_firstname(self):
        return self._is_element_visible(RegistrationPageLocators.FIRSTNAME)

    @allure.step("Проверка видимости поля 'Фамилия'")
    def displayed_lastname(self):
        return self._is_element_visible(RegistrationPageLocators.LASTNAME)

    @allure.step("Проверка видимости поля 'Email'")
    def displayed_email(self):
        return self._is_element_visible(RegistrationPageLocators.EMAIL)

    @allure.step("Проверка видимости поля 'Пароль'")
    def displayed_password(self):
        return self._is_element_visible(RegistrationPageLocators.PASSWORD)

    @allure.step("Проверка видимости поля 'Дата рождения'")
    def displayed_birthday(self):
        return self._is_element_visible(RegistrationPageLocators.BIRTHDAY)

    @allure.step("Нажатие кнопки 'Сохранить' (Зарегистрироваться)")
    def click_save_btn(self):
        self._click(RegistrationPageLocators.SAVE_BTN)

    @allure.step("Выбор пола: {gender}")
    def click_gender_btn(self, gender):
        by, locator_template = RegistrationPageLocators.GENDER_BTN_TEMPLATE
        new_locator = locator_template.format(gender)
        ready_locator = (by, new_locator)
        self._click(ready_locator)

    @allure.step("Отметка всех чекбоксов согласия")
    def click_all_checkboxes(self):
        for i in RegistrationPageLocators.ALL_CHECKBOXES:
            self._click(i)

    @allure.step("Заполнение формы регистрации тестовыми данными")
    def input_values(self):
        self._input_text("test", RegistrationPageLocators.FIRSTNAME)
        self._input_text("testering", RegistrationPageLocators.LASTNAME)
        self._input_text("test@12312.com", RegistrationPageLocators.EMAIL)
        self._input_text("NewPassword1232!", RegistrationPageLocators.PASSWORD)
        self._input_text("03/07/2007", RegistrationPageLocators.BIRTHDAY)
