import pandas as pd 
df = pd.read_csv('planet_data.csv', index_col='eName')
df = df[["isPlanet","meanRadius","orbit_type","orbits"]]


class planet():   #instantiate like this: earth = planet("Earth", "blue", 3)
    def __init__(self,name = "", color = "blue", radius = 1):
        self.color = color
        self.radius = radius
        self.name = name
        self.moon_list = []
class moon():
    def __init__(self,name = "", color = "white", radius = 1,
                     tidally_locked=False, planet_companion =None):
        self.radius = radius
        self.color = color
        self.name = name
        self.tidally_locked = tidally_locked
        self.planet_companion = planet_companion
    def update_planet(self):
        self.planet_companion.moon_list.append(self)

def print_largest(pl):
    largest = None  
    for moon in pl.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius: largest = moon      
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")

planet_d = dict()
moon_d = dict()
for index, row in df.iterrows():
    if row['isPlanet'] is True:
        planet_d[index] = planet(index, radius=row.meanRadius)
        
for index, row in df.iterrows():
    if row['isPlanet'] is False:
        moon_d[index] = moon(index, radius=row.meanRadius, planet_companion=planet_d[row.orbits])


for key, val in planet_d.items():  #now we can check to see what is in our planet dictionary
    print(key, val.radius, val.moon_list)

for key, val in moon_d.items(): #check that the planets got updated
    val.update_planet()
    print(key, val.radius, val.planet_companion.name)

for key, val in planet_d.items():  #get the largest moon for each planet!
    print_largest(val) #sample output: The largest moon of Uranus is Titania
    print(key, [moon.name for moon in val.moon_list]) #sample output: Pluto ['Charon', 'Nix', 'Hydra', 'Kerberos', 'Styx']