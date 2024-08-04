from plates import is_valid

def test_valid_length():
    assert is_valid("AB") == True
    assert is_valid("AB123") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_alphabetic_start():
    assert is_valid("AB123") == True
    assert is_valid("12AB") == False
    assert is_valid("A1B2") == False

def test_invalid_characters():
    assert is_valid("AB 123") == False
    assert is_valid("AB,CD") == False
    assert is_valid("AB!@#") == False
    assert is_valid("AB.CD") == False

def test_leading_zero():
    assert is_valid("AB012") == False
    assert is_valid("AB10") == True
    assert is_valid("AB01") == False
    assert is_valid("A100") == False

def test_digit_placement():
    assert is_valid("AB123") == True
    assert is_valid("AB12C") == False
    assert is_valid("ABC1D") == False
    assert is_valid("123AB") == False
    assert is_valid("AB1CD") == False
