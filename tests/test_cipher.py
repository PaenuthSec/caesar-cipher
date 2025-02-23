import pytest
from cipher import caesar_cipher

test_cases = [

    ("Hello", 3, "encrypt", "Khoor"),
    ("Khoor", 3, "decrypt", "Hello"),
    ("XYZ", 26, "encrypt", "XYZ"),  # Test max shift
    ("Python", 1, "decrypt", "Oxsgm"),
    ("123!@#", 13, "encrypt", "123!@#")
]


@pytest.mark.parametrize("text,shift,mode,expected", test_cases)
def test_caesar_cipher(text, shift, mode, expected):
    assert caesar_cipher(text, shift, mode) == expected