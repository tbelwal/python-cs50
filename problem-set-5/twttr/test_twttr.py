from twttr import shorten


def test_word():
    assert shorten("Beast") == "Bst"


def test_capitals():
    assert shorten("Apples") == "ppls"


def test_lowers():
    assert shorten("happy birthday") == "hppy brthdy"


def test_number():
    assert shorten("CS50") == "CS50"


def test_punctuations():
    assert shorten("Hi! How are you?") == "H! Hw r y?"
