from data_cleaning import *

def test_is_empty():
    assert is_empty('') == True
    assert is_empty(' ') == False
    assert is_empty('0') == False
    assert is_empty('test') == False

def test_is_not_student():
    assert is_not_student('test Faculty') == True
    assert is_not_student('Faculty') == True
    assert is_not_student('000') == False
    assert is_not_student('test') == False

def test_has_year():
    assert has_year('1310') == True
    assert has_year('1982') == True
    assert has_year('1') == True
    assert has_year('99') == True
    assert has_year('') == False
    assert has_year('fac 10') == False
    assert has_year('test') == False

def get_year():
    assert get_year('') == None
    assert get_year('9') == 9
    assert get_year('72') == 72
    assert get_year('1923 - 1933') == 1923
    assert get_year('Fac') == None

def test_add_19():
    assert add_19(8) == 1908
    assert add_19(77) == 1977
    assert add_19(1988) == 1988
    assert add_19(38) == 1938
