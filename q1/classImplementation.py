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

planet1 = Planets("Red", "Gas Giant", False, True, 6)
planet2 = Planets("Blue", "Ice Giant", False, True, 4)

print("--- BEFORE ---")
print(f"Object 1 ({planet1.get_planet_type()}): Moons = {planet1.NumberOfMoons} | {planet1.get_atmosphere_status()}")

print(f"Object 2 ({planet2.get_planet_type()}): Moons = {planet2.NumberOfMoons} | {planet2.get_atmosphere_status()}")
print("-" * 60)

print(f"Performing actions on Object 1 ({planet1.get_planet_type()}) ONLY...")
planet1.rotate()
planet1.MoonCount(67)        
planet1.AtmosphereChange()     
print("-" * 60)

print("--- AFTER ---")
print(f"Object 1 ({planet1.get_planet_type()}): Moons = {planet1.NumberOfMoons} | {planet1.get_atmosphere_status()}")

print(f"Object 2 ({planet2.get_planet_type()}): Moons = {planet2.NumberOfMoons} | {planet2.get_atmosphere_status()}")