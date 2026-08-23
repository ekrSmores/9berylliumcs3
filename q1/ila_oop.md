# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation means putting a certain products detail and actions together into a a class. Rather than using seperate arrays for names, prices, etc. Furthermore, they can only be modified by the necessary functions. This helps prevent accidental logic errors with misuse of the variables. 

### 2. Abstraction
Abstraction helps simplify the complex systems by hiding it and only showing the necessary features for the use. For example, A Class called "Inventory" can provide only addproduct() and Minusproduct(). It does not show the complex systems that is required for the features to work. This helps improve organization and clarity by removing the complexity of the code.

### 3. Inheritance
inheritance can be used to create sub-branches of a certain category without rewriting code for a generic property. An example would be a class called "product" it contains name, price, weight, etc. When something similar is needed to be created like "Beverage", rather than creating another line of code, it can be made as a sub class which can inherit the traits of "product" but can have additional unique traits like mL, DrinkType, etc. It helps improve the clarity by having a clear relationship in the program

### 4. Polymorphism
Polymorphism allows the system to overide the regular feature to execute their own features. For example, a class named "Product" and a subclass called "SaleProduct" and they have a method called TotalCost(price, quantity). But, "SaleProduct" could apply a "buy one get one" or have a discount promo, while "product" only follows the standard price. This helps remove the messy if-else codes entirely to check if a certain product has a certain property.
## Reflection
The four pillar are the foundation in creating a clean systematic programs for markets, games, or applications in general. But if I were to only choose one pillar, I believe encapsulation is the primary choice for me. I believe that encapsulation would be most useful in messy quick environments like supermarkets and sari sari stores. It removes the possibility of entry errors.
