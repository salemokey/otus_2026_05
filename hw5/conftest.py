import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://google.com")

    parser.addoption("--status_code", action="store", type=int, default="404")


@pytest.fixture(scope="session")
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def get_status(request):
    return request.config.getoption("--status_code")
