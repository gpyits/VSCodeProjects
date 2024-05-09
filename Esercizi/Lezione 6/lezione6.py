# Print the age of bob (using the dot notation)
# Create an if-statement that prints the name of the oldest of the two persons
# Create three other Persons. Make a list called people with all 5 Persons
# Make a loop that finds and prints the youngest person’s name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

# Write a class called Student with the attributes name (str) and studyProgram (str)
# Create three instances. One for yourself, one for your left neighbour and one for our right neighbour.
# Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the objects!
# Modify the code and add age and gender to the attributes. Modify your printing methods respectively too.

class Student:
    def __init__(self, name, studyProgram):
        pass

# Given is the class Animal. For each task, test your changes!
# Create two realistic instances of Animals
# Print the name of each object
# Change the amount of legs of one object using the dot notation 
# Add a method setLegs() to set the legs of an object and repeat task 3 but this time using the method.
# Add a method getLegs() to return the amount of legs
# Add a method named printInfo that prints all attributes of the Animal
    
class Animal:
    def __init__(self):
        pass

# Write a new class called Food, it should have name, price and description as attributes.
# Instantiate at least three different foods you know and like.
# Create a new class called Menu, it should have a list (of Foods) as attribute. __init__ should take a list of Foods as optional parameters (default=[])
# Create a addFood() and removeFood() for the Menu
# Create a few new Food instances. Add each to the Menu using the respective Method.
# Add a method printPrices() that list all items on the Menu with their prices.
# Add a Menu method getAveragePrice() that returns the average Food price of the Menu
    
class Food:
    def __init__(self, name, price, descripttion):
        pass

class Menu:
    def __init__(self, default=[]):
        pass