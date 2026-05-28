import pytest

class MockDeliveryService:
    def create(self, order_id):
        return {"delivery_id": 1, "status": "created"}

    def get(self, delivery_id):
        return {"delivery_id": delivery_id, "status": "in_progress"}

    def fail(self, order_id):
        return {"error": "service unavailable", "code": 503}

@pytest.fixture
def mock():
    return MockDeliveryService()

def test_create_delivery(mock):
    result = mock.create(234)
    assert result["delivery_id"] == 1
    assert result["status"] == "created"

def test_id_del(mock):
    assert mock.get(5) == {"delivery_id": 5, "status": "in_progress"}

def test_fail(mock):
    assert mock.fail(455) == {"error": "service unavailable", "code": 503}
