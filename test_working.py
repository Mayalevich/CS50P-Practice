from working import convert
import pytest

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("1:00 AM to 1:00 PM") == "01:00 to 13:00"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 17:00 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00AMto5:00PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
