from abc import ABC

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

    def open(self):
        self._driver.get(self._base_url + self._path)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_visible_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _is_element_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    def _click(self, locator):
        self.wait_clickable(locator).click()

    def _input_text(self, text, locator):
        self.wait_visible(locator).send_keys(text)
