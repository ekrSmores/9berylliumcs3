## Guide Questions

### a. What is duck typing, as explained in the video?
Duck typing is another way to achieving polymorphism besides inheritance. Yet, Objects must have the required attribute or methods.
### b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
The Car class needed to have the same method used by both the cat and the dog so that could that it could work.

###CODE
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)

### How does the code in 2.2 demonstrate polymorphism?
All use the same method but perform a different action. Allowing start_trip function to work with the objects compatible.
