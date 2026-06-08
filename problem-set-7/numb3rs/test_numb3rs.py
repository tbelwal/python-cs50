from numb3rs import validate


def test_valid_ips():
    assert validate("0.0.0.0") is True
    assert validate("1.2.3.4") is True
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True


def test_invalid_range():
    assert validate("256.0.0.1") is False
    assert validate("1.256.0.1") is False
    assert validate("1.2.256.1") is False
    assert validate("1.2.3.256") is False
    assert validate("999.999.999.999") is False


def test_invalid_structure():
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("") is False
    assert validate("1") is False


def test_non_numeric():
    assert validate("cat") is False
    assert validate("1.2.3.cat") is False
    assert validate("cat.2.3.4") is False
    assert validate("1.2.3.4abc") is False


def test_invalid_separators():
    assert validate("123a456b789c000") is False
    assert validate("123-456-789-000") is False
    assert validate("123,456,789,000") is False


def test_leading_zeros():
    assert validate("01.2.3.4") is False
    assert validate("1.02.3.4") is False
    assert validate("1.2.003.4") is False
    assert validate("192.168.001.1") is False
    assert validate("000.0.0.0") is False
