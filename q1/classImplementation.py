class Planets:
    def __init__(self, color: str, planet_type: str, existenceOfLife: bool, PresenceOfAtmosphere: bool, NumberOfMoons: int):
        self.color = color
        self.existenceOfLife = existenceOfLife

        self.NumberOfMoons = NumberOfMoons

        self.__planet_type = planet_type
        self.__PresenceOfAtmosphere = PresenceOfAtmosphere
    def rotate(self):                          
        return f"The {self.__planet_type} is rotating"
    def revolve(self):
        return f"The {self.__planet_type} is revolving around its star"
    def MoonCount(self, amount: int):
        if amount < 0:
            return "Invalid number of moons"
        elif amount == 0:
            return f"The {self.__planet_type} has no moons"
        elif amount > 0:
             return f"The {self.__planet_type} has {amount} moons"