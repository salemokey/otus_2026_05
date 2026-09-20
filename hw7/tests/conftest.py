import pytest
from pom.page.main_page import MainPage
from pom.page.registration_page import RegistrationPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="firefox", help="Выбор браузера: chrome, firefox"
    )
    parser.addoption("--url", default="http://localhost:8081")


@pytest.fixture
def browser(request) -> WebDriver:
    browser_name: str = request.config.getoption("--browser")

    if browser_name == "chrome":
        service: Service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

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
