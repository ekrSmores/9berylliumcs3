# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
I added a new method called "moonCount to know if the planet gains or loses moons.
I removed revolve due to it having no correlation with the planet and changed it into AtmosphereChange
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
| Color     | str       | Public     | The color of the planet can be changed due to it's probability of changing climates|
| PlanetType | str | Private | Once a type of planet is classified it can't turn into other types |
| ExistenceOfLife | bool | Public | There is a possible chance that life can grow or die |
| PresenceOfAtmosphere | bool | Private | Identical to "PlanetType", it is usually not change and stays a constant whether it has a atmosphere or not |
| NumberOfMoons | int | Public | It is public because the moons could collide with the planet they're orbitting |
## Updated UML Class Diagram
![Class Diagram](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/images/PLANETSNEW.png)
## Python Implementation

[View Python Source](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/classImplementation.py)
## Test Run
![Test Run](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/images/ClassTestRun.png)
## Object Diagram
![Object Diagram](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/images/ObjectDiagram.png)

## Short Analysis

### Why did you make your chosen attribute private?
1. Why did you make your chosen attribute private? Explain what could go wrong if other parts of the
program changed it directly.
I chose to make Planet_type private because if it were to be changed directly the logic would not add up. Similarly, The PresenceOfAtmosphere is also private due to if it were to be present it would'nt make sense and it is suppose to be tied up with the Planet_type.
### Which method changes the state of your object?
2. Which method changes the state of your object? Identify the attribute affected and describe what
happens.
The MoonCount and AtmosphereChange are the methods which changes the state of my object. MoonCount adds or Destroys moons depending on the given number, it can represent the moons colliding or being taken by the gravitional force of the planet. AtmosphereChange toggles the presence of the atmosphere from true or false.

### How did your two objects demonstrate that instances are independent?
3. How did your two objects demonstrate that instances are independent? Refer to your actual test
output.
After the results were given, it is shown that planet1 had 73 moons and lost its atmosphere. While, planet2 was shown to be constant and unaffected keeping its orginal attributes their respective values.
### What is the difference between your class diagram and your object diagram?
4. What is the difference between your class diagram and your object diagram? Explain this using your
own class.
The class diagram acts as the blueprint, while the object diagram shows the blueprint in action. The class diagram shows the attributes, data types, visibility, and methods. While on the otherhand, the object diagram shows the resulting values after the changes, an example would be planet 1 gaining 67 moons prior from a measly 6 moons. 