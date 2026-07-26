import requests
import pytest


def test_request_url(get_url, get_status):
    url = get_url
    url_response = requests.get(url)

    assert url_response.status_code == int(get_status)
