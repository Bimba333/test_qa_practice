import pytest

def complete_trip(driver, distance_km):
    driver["trips"] += 1
    return distance_km * 15



class OrderService:
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def count(self):
        return len(self.orders)

    def find_by_city(self, city):
        return [o for o in self.orders if o["city"] == city]

@pytest.fixture
def order_service():
    return OrderService()

@pytest.fixture
def warehouse():
    return{"apple": 100, "banana": 50, "mango": 0}

@pytest.fixture
def driver():
    return {"name": "Иван", "trips": 0, "rating": 5.0}


def test_warehouse_has_apple(warehouse):
    assert "apple" in warehouse
def test_mango_out_of_stock(warehouse):
    assert warehouse["mango"] == 0
def test_all_quantities_non_negative(warehouse):
    for item in warehouse.values():
        assert item >= 0


def test_complete_trip(driver):
    assert complete_trip(driver, 50) == 750
    assert driver.get("trips") == 1


def test_adding(order_service):
    order_service.add({"id": 1, "city": "Москва"})
    order_service.add({"id": 2, "city": "Москва"})
    assert order_service.count() == 2

def test_count_msk(order_service):
    order_service.add({"id": 1, "city": "Москва"})
    order_service.add({"id": 2, "city": "Казань"})
    order_service.add({"id": 3, "city": "Москва"})
    result = order_service.find_by_city("Москва")
    assert len(result) == 2

def test_count_sochi(order_service):
    order_service.add({"id": 1, "city": "Москва"})
    order_service.add({"id": 2, "city": "Казань"})
    order_service.add({"id": 3, "city": "Москва"})
    result = order_service.find_by_city("Сочи")
    assert len(result) == 0