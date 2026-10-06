import logging

import pytest
from pom.page.main_page import MainPage
from pom.page.registration_page import RegistrationPage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="Выбор браузера: chrome, firefox")
    parser.addoption("--url", default="http://localhost:8081")
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="session", autouse=True)
def init_logging():

    log_level = logging.DEBUG

    log_format = "%(asctime)s [%(levelname)s] (%(name)s) %(message)s"

    logging.basicConfig(
        level=log_level,
        handlers=[logging.StreamHandler()],
        format=log_format,
        force=True,
    )

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("selenium").setLevel(logging.WARNING)
    logging.getLogger("WDM").setLevel(logging.WARNING)


@pytest.fixture
def browser(request) -> WebDriver:
    browser_name: str = request.config.getoption("--browser")
    headless: bool = request.config.getoption("--headless", default=False)

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

        options.binary_location = "/usr/bin/chromium"

        service: Service = webdriver.ChromeService("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")

        options.binary_location = "/usr/bin/firefox-esr"

        service: Service = webdriver.FirefoxService("/usr/bin/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)

    if not headless:
        driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def base_url(request) -> str:
    return request.config.getoption("--url")


@pytest.fixture
def main_page(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()
    return page


@pytest.fixture
def login_page(main_page):
    return main_page.click_on_login()


@pytest.fixture
def registration_page(browser, base_url):
    page = RegistrationPage(browser, base_url)
    page.open()
    return page


@pytest.fixture
def product_page(main_page):
    return main_page.click_on_product()


@pytest.fixture
def cart_page(product_page):
    return product_page.open_cart_from_modal()
