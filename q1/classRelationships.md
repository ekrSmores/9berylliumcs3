## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class:Planets
Description:A class that show the characteristics of a planet
## New Related Class
Class:System
Description:a class that shows the system wherein the planets live in
## Association
Relationship: System > planet
Explanation: Planets are a part of planets
## Multiplicity

Multiplicity: Many to one
Explanation: Systems have many planets 
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
