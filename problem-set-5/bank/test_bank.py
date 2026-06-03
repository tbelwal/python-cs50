from bank import value


def test_hello():
    assert value("Hello!") == 0
    assert value("hello") == 0
    assert value("hello!") == 0
    assert value("hello.") == 0


def test_h_only():
    assert value("Hi") == 20
    assert value("How are you") == 20
    assert value("hi    ") == 20


def test_no_greeting():
    assert value("Good day") == 100
