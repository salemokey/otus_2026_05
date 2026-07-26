import requests
import pytest
import json


@pytest.fixture
def check_api():

    def _make_request(url):
        resp = requests.get(url)
        data = resp.json()

        # assert resp.status_code == 200
        assert data["status"] == "success"
        assert isinstance(data, dict)
        return data

    return _make_request


@pytest.mark.dog_api_list_all
def test_alldogs_list(check_api):

    url = "https://dog.ceo/api/breeds/list/all"
    data = check_api(url)
    assert "african" in data["message"]
    assert 0 < len(data["message"])
    assert any(data["message"].values())


@pytest.mark.dog_image_random
def test_image_random(check_api):
    url = "https://dog.ceo/api/breeds/image/random"
    data = check_api(url)


url_list_breeds = "https://dog.ceo/api/breeds/list"
response = requests.get(url_list_breeds)
response_json = response.json()


@pytest.mark.parametrize("breed", list(response_json["message"]))
@pytest.mark.dog_breed_img
def test_breed_img(check_api, breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    data = check_api(url)


sub_breeds_list = []
for breed in response_json["message"]:
    url = f"https://dog.ceo/api/breed/{breed}/list"
    response = requests.get(url)
    response_json = response.json()

    if len(response_json["message"]) > 0:
        for sub_breed in response_json["message"]:
            sub_breeds_list.append((breed, sub_breed))


@pytest.mark.parametrize("breed, sub_breed", sub_breeds_list)
@pytest.mark.dog_sub_breed_img
def test_sub_breed_img(check_api, breed, sub_breed):

    if breed == "danish":
        pytest.skip(f"Пропускаем породу {breed}, так как API часто возвращает ошибку")

    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
    data = check_api(url)

    assert len(data) > 0


# test_dogapi()
