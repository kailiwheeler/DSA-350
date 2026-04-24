from data_cleaning import *

def test_is_empty():
    assert is_empty('') is True
    assert is_empty(' ') is False
    assert is_empty('0') is False
    assert is_empty('test') is False

def test_is_not_student():
    assert is_not_student('test Faculty') is True
    assert is_not_student('Faculty') is True
    assert is_not_student('000') is False
    assert is_not_student('test') is False

def test_has_year():
    assert has_year('1310') is True
    assert has_year('1982') is True
    assert has_year('1') is True
    assert has_year('99') is True
    assert has_year('') is False
    assert has_year('fac 10') is False
    assert has_year('test') is False

def test_get_year():
    assert get_year('') is None
    assert get_year('9') == 9
    assert get_year('72') == 72
    assert get_year('1923 - 1933') == 1923
    assert get_year('Fac') is None

def test_add_19():
    assert add_19(8) == 1908
    assert add_19(77) == 1977
    assert add_19(1988) == 1988
    assert add_19(38) == 1938
