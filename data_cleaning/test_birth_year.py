from data_cleaning import *

def test_has_birthday_field():
    assert has_birthday_field('') is False
    assert has_birthday_field('12/15/1900') is True

def test_has_birth_year():
    assert has_birth_year('') is False
    assert has_birth_year('Died: 04/09/1948') is False
    assert has_birth_year('DOD: 10/2009') is False
    assert has_birth_year('DOB: ??????') is False
    assert has_birth_year('DOB: UNK Died: 03/31/06') is False
    assert has_birth_year('DOB: October 1966') is True
    assert has_birth_year('DOB:07/09/1916') is True
    assert has_birth_year('DOB:08/29/12 Died: 1992') is True
    assert has_birth_year('DOB:09/14/13 DOD:11/16/04"') is True

def test_get_birth_year():
    assert get_birth_year('DOB: October 1966') == 1966
    assert get_birth_year('6/10/4319') == 4219 #will end up throwing that value out
    assert get_birth_year('7/1/2066') == 1966
    assert get_birth_year('DOB:07/09/1916') == 1916
    assert get_birth_year('DOB:08/29/12 Died: 1992') == 1912
    assert get_birth_year('DOB:09/14/13 DOD:11/16/04"') == 1913