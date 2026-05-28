import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def todos():
    response_list = requests.get(f"{BASE_URL}/todos")
    return response_list

@pytest.fixture(scope="module")
def todo():
    response_get = requests.get(f"{BASE_URL}/todos/5")
    return response_get

def test_stat_code_todos(todos):
    assert todos.status_code == 200
def test_valid_type(todos):
    assert isinstance(todos.json(), list)
def test_non_empty(todos):
    assert todos.json()
def test_has(todos):
    assert "id" in todos.json()[0]
    assert "title" in todos.json()[0]
    assert "completed" in todos.json()[0]

def test_stat_code_todo(todo):
    assert todo.status_code == 200
def test_valid_id(todo):
    assert todo.json()["id"] == 5

def test_stat_code_negative():
    assert requests.get(f"{BASE_URL}/todos/99999").status_code == 404   

