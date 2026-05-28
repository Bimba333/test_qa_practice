import pytest
from get_order_status import get_order_status 

@pytest.mark.parametrize("order, expect", [
    ({"id": 1, "status": "NEW"}, "new"),
    ({"id": 2, "status": "Done"}, "done"),
    ({"id": 3, "city": "Москва"}, "unknown")
]
) 
def test_valid_order_status(order, expect):
    assert get_order_status(order) == expect