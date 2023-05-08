import pytest

from task2.task2 import Bytes

TEST_DATA = [
    ("2084 MB", "3 KB", "!=", True),
    ("1984 B", "8 MB", "==", True),
    ("8 KB", "6000 B", ">", False),
    ("24 KB", "2354389 MB", "<", True),
    ("38 B", "38 B", "!=", True),
    ("1024 B", "1 KB", "==", False),
    ("1025 KB", "1 MB", ">", True),
    ("1023 KB", "1 MB", "<", True),
]

@pytest.mark.parametrize("first_data, second_data, operator, expected", TEST_DATA)
def test_bytes_comparison(first_data, second_data, operator, expected):
    b1 = Bytes(first_data)
    b2 = Bytes(second_data)

    if operator == "==":
        assert (b1 == b2) == expected
    elif operator == "!=":
        assert (b1 != b2) == expected
    elif operator == ">":
        assert (b1 > b2) == expected
    elif operator == "<":
        assert (b1 < b2) == expected
