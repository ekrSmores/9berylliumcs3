# advancedRelationships.py
# My OOP Space System - Part IV: Advanced Class Relationships

class Planets:
    """Parent Class representing a foundational Planet entity."""
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

    def strip_atmosphere(self):
        """Safely mutates internal state without external name-mangling."""
        self.__PresenceOfAtmosphere = False

    def rotate(self):                          
        return f"The {self.__planet_type} is rotating."


class GasGiant(Planets):
    """Child Class demonstrating INHERITANCE (IS-A Relationship)."""
    def __init__(self, color: str, existenceOfLife: bool, PresenceOfAtmosphere: bool, NumberOfMoons: int, has_rings: bool, gas_density: str):
        # Using super().__init__() to reuse parent class initialization code
        super().__init__(color, "Gas Giant", existenceOfLife, PresenceOfAtmosphere, NumberOfMoons)
        self.has_rings = has_rings  # Unique child attribute
        self.gas_density = gas_density  # Added gas density attribute

    def display_ring_info(self):
        ring_status = "possesses a planetary ring system" if self.has_rings else "does not have rings"
        return f"This Gas Giant {ring_status} with a gas density of {self.gas_density}."


class StarCore:
    """Component Class demonstrating COMPOSITION (Part of the system)."""
    def __init__(self, core_temperature: str, energy_output: str):
        self.core_temperature = core_temperature
        self.energy_output = energy_output

    def get_core_details(self) -> str:
        return f"Core Temp: {self.core_temperature} | Energy: {self.energy_output}"


class system:
    """Whole Class managing both Composition (StarCore) and Association (Planets)."""
    def __init__(self, SunColor: str, Suntype: str, existenceOfLife: bool, NumberOfPlanets: int, planets: list = None):
        self.SunColor = SunColor
        self.Suntype = Suntype
        self.existenceOfLife = existenceOfLife
        self.NumberOfPlanets = NumberOfPlanets
        self.planets = planets if planets is not None else []
        
        # COMPOSITION: StarCore is created inside the System lifecycle
        self.core = StarCore("15 Million Kelvin", "3.8 x 10^26 Watts")

    def Supernova(self):
        print(f"\n💥 SYSTEM CRITICAL: The {self.Suntype} core at {self.core.get_core_details()} is collapsing!")
        for planet in self.planets:
            planet.existenceOfLife = False
            planet.NumberOfMoons = 0
            planet.strip_atmosphere() 
            print(f"💥 The supernova has stripped the atmosphere, destroyed all moons, and wiped out life on the {planet.get_planet_type()}!")
        
        # Destroying the composite part along with the system
        self.core = None
        raise Exception("💥 The star has gone supernova! The system and its StarCore are destroyed.")


# ==========================================
# TEST PIPELINE RUN
# ==========================================
if __name__ == "__main__":
    print("--- BEFORE ---")
    planet1 = GasGiant("Orange/White", False, True, 79, has_rings=True, gas_density="1.33 g/cm³")
    planet2 = Planets("Blue", "Ice Giant", False, True, 4)

    system1 = system("Yellow", "Main Sequence", True, 2, [planet1, planet2])

    print(f"Object 1 ({planet1.get_planet_type()}): Moons = {planet1.NumberOfMoons} | {planet1.get_atmosphere_status()} | {planet1.display_ring_info()}")
    print(f"Object 2 ({planet2.get_planet_type()}): Moons = {planet2.NumberOfMoons} | {planet2.get_atmosphere_status()}")
    print("-" * 60)
    print(f"System 1 Core Status: {system1.core.get_core_details()}")
    print("-" * 60)
    print("--- AFTER ---")

    try:
        system1.Supernova()
    except Exception as e:
        print(e)
