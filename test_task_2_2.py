import pytest
from classify_weight import classify_weight

@pytest.mark.parametrize("kg, expect" , [
    (0, None),
    (0.5, "light"),
    (1, "medium"),
    (10, "medium"),
    (10.001, "heavy"),
    (50, "heavy")
]
)
def test_classify_weight(kg, expect):
    assert classify_weight(kg) == expect