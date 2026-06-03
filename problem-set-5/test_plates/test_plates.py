from plates import is_valid


def test_valid_plate():
    assert is_valid("AB1122")
    assert is_valid("ASS380")


def test_numbers():
    assert not is_valid("010101")
    assert not is_valid("WE0077")
    assert is_valid("HOt456")


def test_length():
    assert is_valid("ABCDEF")
    assert is_valid("WET790")
    assert is_valid("Acid")
    assert not is_valid("Act123456")


def test_punctuations():
    assert not is_valid("!nimal")
