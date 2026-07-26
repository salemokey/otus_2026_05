import requests
import pytest
import json


def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resp = requests.get(url)
    data = resp.json()

    assert resp.status_code == 200
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    post = {"title": "testitle", "body": "testbody", "userid": 123}

    headers = {"Content-type": "application/json"}

    response = requests.post(url, data=json.dumps(post), headers=headers)

    response_json = response.json()
    assert response.status_code == 201
    assert response_json.get("id")
    assert response_json["title"] == post["title"]
    assert response_json["body"] == post["body"]
    assert response_json["userid"] == post["userid"]


def test_get_filter_post():
    url = "https://jsonplaceholder.typicode.com/posts?userId=10"
    response = requests.get(url)
    response_json_post = response.json()

    assert response_json_post[0]["userId"] == 10
    for item in response_json_post:
        if item["id"] == 92:
            assert True


response_user = requests.get("https://jsonplaceholder.typicode.com/users")
response_user_json = response_user.json()

list_names_users = [data["name"] for data in response_user_json]


@pytest.mark.parametrize("name", list_names_users)
def test_get_users(name):
    filter_name = name
    url = f"https://jsonplaceholder.typicode.com/users?name={filter_name}"
    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json) > 0
    for user in response_json:
        assert user["name"] == filter_name


response_post_comments = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1/comments"
)
response_post_comments_json = response_post_comments.json()

list_names_emails = [data["email"] for data in response_post_comments_json]


@pytest.mark.parametrize("email", list_names_emails)
def test_get_comment(email):
    response_filtered_comments = requests.get(
        f"https://jsonplaceholder.typicode.com/comments?email={email}"
    ).json()

    for item in response_filtered_comments:
        assert item["email"] == email
