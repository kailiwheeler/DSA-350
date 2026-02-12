from planet_classes import planet
from planet_classes import moon
from planet_classes import print_largest


def test_planet_defaults():
    temp1 = planet()
    assert temp1.name == ""
    assert temp1.color == "blue"
    assert temp1.radius == 1
    assert temp1.moon_list == []
def test_moon_defaults():
    temp2 = moon()
    assert temp2.name == ""
    assert temp2.color == "white"
    assert temp2.radius == 1
    assert temp2.tidally_locked == False
    assert temp2.planet_companion == None
def test_planet_value():
    Earth = planet("Earth", "green", 3)
    assert Earth.name == "Earth"
    assert Earth.color == "green"
    assert Earth.radius == 3
    assert Earth.moon_list == []
def test_moon_values():
    Luna = moon("Luna", "grey", 0.5, True)
    assert Luna.name == "Luna"
    assert Luna.color == "grey"
    assert Luna.radius == 0.5
    assert Luna.tidally_locked == True
    assert Luna.planet_companion == None
def test_planet_with_moons():
    Mars = planet("Mars", "red", 2)
    Phobos = moon("Phobos", "orange", 1, True, Mars)
    Deimos = moon("Diemos", "tan", 0.5, True, Mars)
    Phobos.update_planet()
    Deimos.update_planet()
    assert len(Mars.moon_list) == 2
    
