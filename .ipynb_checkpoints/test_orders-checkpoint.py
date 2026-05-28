import pytest
from orders import is_valid_order

@pytest.mark.parametrize("order, expected", [
    ({"id": 1, "city": "Москва", "price": 1500}, True),   
    ({"id": 2, "city": "Казань", "price": 0}, False),   
    ({"id": 3, "city": "", "price": 100}, False),   
    ({"id": 4, "city": "Сочи"}, False),   
    ({"id": 5, "city": 123, "price": 100}, False),   
  ], ids=[
        "valid_order",
        "zero_price",
        "empty_city",
        "missing_price",
        "city_not_string",
    ])
def test_is_valid_order(order, expected):
    assert is_valid_order(order) == expected

@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "city": "Москва", "price": 1500},
        {"id": 2, "city": "Йемен", "price": 2222},
        {"id": 3, "city": "Лондон", "price": 3333}
    ]

def test_all_orders_have_id(sample_orders):
    for order in sample_orders:
        assert "id" in order

def test_orders_count(sample_orders):
    assert len(sample_orders) == 3

def test_no_negative_prices(sample_orders):
    for order in sample_orders:
        assert order["price"] > 0