import pytest
from datetime import date
from seasons import calculate_minutes, convert_to_words

def test_calculate_minutes():
    assert calculate_minutes(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert calculate_minutes(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
    assert calculate_minutes(date(1995, 1, 1), date(2000, 1, 1)) == 2629440
    assert calculate_minutes(date(2020, 6, 1), date(2032, 1, 1)) == 6092640
    assert calculate_minutes(date(1998, 6, 20), date(2000, 1, 1)) == 806400

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred"
    assert convert_to_words(2629440) == "Two million, six hundred twenty-nine thousand, four hundred forty"
    assert convert_to_words(6092640) == "Six million, ninety-two thousand, six hundred forty"
    assert convert_to_words(806400) == "Eight hundred six thousand, four hundred"
