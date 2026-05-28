import pytest
from delivery import calculate_delivery_cost

@pytest.mark.parametrize("distance_km, weight_kg, expect", [
    (100, 10, 1050),
    (0, 10, None),
    (50, -3, None),
] 
)
def test_is_valid_delivery(distance_km, weight_kg, expect):
    assert calculate_delivery_cost(distance_km, weight_kg) == expect