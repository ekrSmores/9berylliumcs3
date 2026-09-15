class Planets:
    def __init__(self, color: str, planet_type: str, existenceOfLife: bool, PresenceOfAtmosphere: bool, NumberOfMoons: int):
        self.color = color
        self.existenceOfLife = existenceOfLife
        self.NumberOfMoons = NumberOfMoons
        
        self.__planet_type = planet_type
        self.__PresenceOfAtmosphere = PresenceOfAtmosphere

    def get_planet_type(self):
        return self.__planet_type

    def get_atmosphere_status(self):
        status = "has" if self.__PresenceOfAtmosphere else "does not have"
        return f"It {status} an atmosphere."

    def rotate(self):                          
        return f"The {self.__planet_type} is rotating"

    def AtmosphereChange(self):
        if self.__PresenceOfAtmosphere:
            self.__PresenceOfAtmosphere = False
            print(f"📡 Notice: The atmosphere of the {self.__planet_type} has been stripped away.")
        else:
            self.__PresenceOfAtmosphere = True
            print(f"📡 Notice: An atmosphere has formed on the {self.__planet_type}.")
        return self.__PresenceOfAtmosphere
    
    def MoonCount(self, amount: int):
        if amount + self.NumberOfMoons >= 0:
            self.NumberOfMoons += amount
            print(f"{amount} moons updated for the {self.__planet_type}. Total: {self.NumberOfMoons}")
        else:
            print("Invalid configuration Moon count cannot be negative")
        return self.NumberOfMoons


class system:
    # 1. Added 'planets' to the arguments so the system can hold them
    def __init__(self, SunColor: str, Suntype: str, existenceOfLife: bool, NumberOfPlanets: int, planets: list = []):
        self.SunColor = SunColor
        self.Suntype = Suntype
        self.existenceOfLife = existenceOfLife
        self.NumberOfPlanets = NumberOfPlanets
        self.planets = planets # Keeps track of this system's planets

    def Supernova(self):
        for planet in self.planets:
            planet.existenceOfLife = False
            planet.NumberOfMoons = 0
            planet._Planets__PresenceOfAtmosphere = False 
            print(f"💥 The supernova has stripped the atmosphere, destroyed all moons, and wiped out life on the {planet.get_planet_type()}!")

        raise Exception("💥 The star has gone supernova! The system is destroyed.")

    
    def PlanetCount(self, amount: int):
        if amount + self.NumberOfPlanets >= 0:
            self.NumberOfPlanets += amount
            print(f"{amount} planets updated for the {self.Suntype}. Total: {self.NumberOfPlanets}")
        else:
            print("Invalid configuration Planet count cannot be negative")
        return self.NumberOfPlanets

planet1 = Planets("Red", "Gas Giant", False, True, 6)
planet2 = Planets("Blue", "Ice Giant", False, True, 4)

# 3. Passed the planet objects into their respective systems
system1 = system("Yellow", "Main Sequence", True, 2, [planet1, planet2])
system2 = system("Red", "Red Giant", False, 1)

print("--- BEFORE ---")
print(f"Object 1 ({planet1.get_planet_type()}): Moons = {planet1.NumberOfMoons} | {planet1.get_atmosphere_status()}")
print(f"Object 2 ({planet2.get_planet_type()}): Moons = {planet2.NumberOfMoons} | {planet2.get_atmosphere_status()}")
print("-" * 60)
print(f"System 1 ({system1.Suntype}): Planets = {system1.NumberOfPlanets}")
print(f"System 2 ({system2.Suntype}): Planets = {system2.NumberOfPlanets}")
print("-" * 60)
print("--- AFTER ---")

try:
    system1.Supernova()
except Exception as e:
    print(e)

print("-" * 60)
print(f"Object 1 ({planet1.get_planet_type()}): Moons = {planet1.NumberOfMoons} | {planet1.get_atmosphere_status()}")
print(f"Object 2 ({planet2.get_planet_type()}): Moons = {planet2.NumberOfMoons} | {planet2.get_atmosphere_status()}")
