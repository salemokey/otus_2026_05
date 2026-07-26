import requests
import pytest


@pytest.fixture
def check_api():

    def _make_request(url):
        resp = requests.get(url)
        data = resp.json()

        assert resp.status_code == 200
        if isinstance(data, list):
            assert isinstance(data[0]["id"], str)
            assert isinstance(data[0]["name"], str)
            assert isinstance(data[0]["brewery_type"], str)
            assert isinstance(data[0]["address_1"], (str, type(None)))
            assert isinstance(data[0]["address_2"], (str, type(None)))
            assert isinstance(data[0]["address_3"], (str, type(None)))
            assert isinstance(data[0]["city"], str)
            assert isinstance(data[0]["state_province"], (str, type(None)))
        elif isinstance(data, dict):
            assert isinstance(data["id"], str)
            assert isinstance(data["name"], str)
            assert isinstance(data["brewery_type"], str)
            assert isinstance(data["address_1"], (str, type(None)))
            assert isinstance(data["address_2"], (str, type(None)))
            assert isinstance(data["address_3"], (str, type(None)))
            assert isinstance(data["city"], str)
            assert isinstance(data["state_province"], (str, type(None)))

        # assert data["status"] == "success"
        # assert isinstance(data, dict)
        return data

    return _make_request


@pytest.mark.random_brewery
def test_random_brewery(check_api):
    url = "https://api.openbrewerydb.org/v1/breweries/random"
    data = check_api(url)


def test_single_brewery(check_api):
    random_data = check_api("https://api.openbrewerydb.org/v1/breweries/random")
    random_id = random_data[0]["id"]

    single_data = check_api(f"https://api.openbrewerydb.org/v1/breweries/{random_id}")

    assert single_data["name"] == random_data[0]["name"]


list_cities = ["San Diego", "Odessa", "Dallas", "Austin"]


@pytest.mark.parametrize("city", ["San Diego", "Odessa", "Houston", "Austin"])
def test_search_breweries(check_api, city):
    new_city = city.replace(" ", "%20").lower()
    url = f"https://api.openbrewerydb.org/v1/breweries/search?query={new_city}"
    data = check_api(url)

    assert len(data) > 0, "0 результатов"
    for item in data:
        assert city.lower() in item["city"].lower() or item["name"].lower()


@pytest.mark.parametrize("city", ["San Diego", "Odessa", "Houston", "Austin"])
def test_by_city_breweries(check_api, city):
    new_city = city.replace(" ", "_").lower()
    url = f"https://api.openbrewerydb.org/v1/breweries?by_city={new_city}&per_page=3"
    data = check_api(url)

    assert len(data) == 3
    for item in data:
        assert city.lower() in item["city"].lower()
