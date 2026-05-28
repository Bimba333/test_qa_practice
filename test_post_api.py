import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def todo():
    response = requests.post(
        f"{BASE_URL}/todos",
        json={
            "title": "Доставить заказ в Москву",
            "completed": False,
            "userId": 1
        }
    )
    return response


def test_create_todo_status_code(todo):
    assert todo.status_code == 201
def test_create_todo_returns_id(todo):
    assert "id" in todo.json()
def test_create_todo_title_matches(todo):
    assert todo.json()["title"] == "Доставить заказ в Москву"