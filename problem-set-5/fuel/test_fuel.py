from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("-3/6")
