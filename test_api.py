import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_todo_status_code():
    response = requests.get(f"{BASE_URL}/todos/1")
    assert response.status_code == 200

def test_get_todo_has_required_fields():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "completed" in data
    assert "userId" in data

def test_get_todo_correct_id():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert data["id"] == 1

def test_get_todo_completed_is_bool():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert isinstance(data["completed"], bool)

def test_get_nonexistent_todo():
    response = requests.get(f"{BASE_URL}/todos/99999")
    assert response.status_code == 404