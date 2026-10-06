import logging
from abc import ABC

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AbsBasePage(ABC):
    _driver: WebDriver

    def __init__(self, browser, base_url, path: str):
        self._driver = browser
        self._base_url = base_url
        self._path = path
        self.wait = WebDriverWait(browser, 10)
        self.logger = logging.getLogger("BasePage")

    def open(self):
        self.logger.info("Переходим по адресу: %s", self._base_url + self._path)
        self._driver.get(self._base_url + self._path)

    def wait_visible(self, locator):
        self.logger.debug("Ожидание видимости: %s", locator)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_visible_all(self, locator):
        self.logger.debug("Ожидание отображения элемента %s", locator)
        try:
            element = self.wait.until(EC.visibility_of_all_elements_located(locator))
            count = len(element)
            self.logger.debug("Элементы %s найдены в количестве %d и видны.", locator, count)
            return element
        except TimeoutException:
            self.logger.warning("Элементы %s НЕ появились на странице за отведенное время.", locator)
            raise

    def wait_clickable(self, locator):
        self.logger.debug("Ожидание кликабельноного элемента: %s", locator)
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.logger.debug("Элемент %s найден и виден.", locator)
            return element
        except TimeoutException:
            self.logger.warning("Элемент %s НЕ появился на странице за отведенное время.", locator)
            raise

    def _is_element_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            self.logger.debug("Элемент %s найден и виден.", locator)
            return True
        except NoSuchElementException:
            self.logger.warning("Элемент %s не виден.", locator)
            return False

    def _click(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            try:
                element = self.wait_clickable(locator)
                element.click()
            except ElementClickInterceptedException as e:
                self.logger.error(f"НЕ удалось кликнуть по элементу {locator}. Ошибка: {e}")
                raise

    def _input_text(self, text, locator):
        with allure.step(f"Ввод текста {text} в поле {locator}"):
            try:
                element = self.wait_visible(locator)
                element.clear()
                element.send_keys(text)
            except ElementNotInteractableException as e:
                self.logger.error(f"Ошибка ввода текста в {locator}: {e}")
                raise

    def get_screenshot_png(self) -> bytes:
        self._driver.get_screenshot_as_png()
