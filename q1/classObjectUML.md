## Design Revision
No major changes were needed from my original design.
------------------------------------------------------
# SG4 - Understanding Classes and Objects
## Planets
## A class that reperesents the possible things a planet has. 
## Properties
| Property | Data Type | Description |
|Color|String |General Color of the planet.|
|PlanetType| String | Whether it may be a gas giant, dwarf plant, etc.|
|ExistenceOfLife | Boolean | If life exist within the planet |
|PresenceOfAtmosphere | Boolean | If the planet has an atmosphere|
|NumberOfMoons | Integer |Number of Natural sattelites the planet has. |
## Methods
| Method | Description |
| Rotate | The way the planet spins on its axis|
| Revolve | The way the planet revolves around its star.|
| MoonCount | A moon could crash with the planet which still could create more smaller moons or none whatsoever |
## Attribute Changes
| Attribute | Data Type | Visibility | Reason |
| Color     | str       | Public     | The color of the planet can be changed due to it's probability of changing climates|
| PlanetType | str | Private | Once a type of planet is classified it can't turn into other types |
| ExistenceOfLife | bool | Public | There is a possible chance that life can grow or die |
| PresenceOfAtmosphere | bool | Private | Identical to "PlanetType", it is usually not change and stays a constant whether it has a atmosphere or not |
| NumberOfMoons | int | Public | It is public because the moons could collide with the planet they're orbitting |
## Class Diagram
![Class Diagram](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/images/PLANETS.png)
## Updated Class Diagram
![UPD Class Diagram](https://github.com/ekrSmores/9berylliumcs3/blob/main/q1/images/PLANETSNEW.png)
## Design Explanation
### Why did you choose this class?
I chose this class because it is where im most interested at, astronomy. It would act as a contribution to my love in sciences and astronomy
### Which property is the most important? Why?
The most important propety would be the planet type because it could affect the other properties like color, existence of life, and presence of atmosphere.
### Which method is the most useful? Why?
While rotate is the most commonly used, the revolve is the most useful because if the planet does not revolve around its sun it would drift out of it system this becoming a rogue planet