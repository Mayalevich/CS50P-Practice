from twttr import shorten

def test_shorten_with_vowels():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("AEIOUaeiou") == ""

def test_shorten_with_no_vowels():
    assert shorten("gym") == "gym"
    assert shorten("why") == "why"

def test_shorten_with_characters_numbers_and_symbols():
    assert shorten("1234!@#$") == "1234!@#$"
    assert shorten("A1E2I3O4U5") == "12345"
