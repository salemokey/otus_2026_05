import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


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
