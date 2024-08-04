from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("99/100") == 99
    assert convert("1/100") == 1

    try:
        convert("2/1")
        assert False
    except ValueError:
        assert True
    try:
        convert("1/0")
        assert False
    except ZeroDivisionError:
        assert True
    try:
        convert("abc/def")
        assert False
    except ValueError:
        assert True
    try:
        convert("3.5/7")
        assert False
    except ValueError:
        assert True


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(98) == "98%"
