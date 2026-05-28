import pytest
from is_valid_email import is_valid_email

@pytest.mark.parametrize("email, expect", [
    ("test@example.com", True),
    ("user@mail.ru", True),
    ("notanemail", False),
    ("two@@mail.com", False),
    ("@mail.com", False),
    ("user@nodot", False)
]
)
def test_is_valid_email(email, expect):
    assert is_valid_email(email) == expect