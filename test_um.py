from um import count

def test_single():
    assert count("hello, um, world") == 1

def test_multiple():
    assert count("um, hello, um, how are you? um") == 3

def test_no():
    assert count("hello, world!") == 0

def test_in_word():
    assert count("yummy, um, umbrella") == 1

def test_case_insensitivity():
    assert count("Um, um, UM") == 3
