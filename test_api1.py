import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def todo():
    return requests.get(f"{BASE_URL}/todos/1")

def test_status_code(todo):
    assert todo.status_code == 200

def test_has_required_fields(todo):
    data = todo.json()
    assert "id" in data
    assert "title" in data
    assert "completed" in data

def test_correct_id(todo):
    assert todo.json()["id"] == 1