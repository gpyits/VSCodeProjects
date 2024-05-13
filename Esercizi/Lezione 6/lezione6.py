# Print the age of bob (using the dot notation)
# Create an if-statement that prints the name of the oldest of the two persons
# Create three other Persons. Make a list called people with all 5 Persons
# Make a loop that finds and prints the youngest person’s name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
alice, bob, marco, giovanni, marta= Person("Alice W.", 45), Person("Bob M.", 36), Person('marco', 100), Person('giovanni', 20), Person('marta', 40)
people=[bob, alice, marco, giovanni, marta]
print(bob.name)
print(bob.age) if bob.age>alice.age else print(alice.age)
print(min([(person.age, person.name) for person in people])[1])

# Write a class called Student with the attributes name (str) and studyProgram (str)
# Create three instances. One for yourself, one for your left neighbour and one for our right neighbour.
# Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the objects!
# Modify the code and add age and gender to the attributes. Modify your printing methods respectively too.

class Student:
    def __init__(self, name, age, gender, studyProgram):
        self.name=name
        self.age=age
        self.gender=gender
        self.studyProgram=studyProgram
    def printInfo(self):
        print(self.name, self.age, self.gender, self.studyProgram)

myself, rightself, leftself=Student('Pippo', 20, 'M', 'Cybersec'), Student('Pluto', 31, 'M', 'Maths'), Student('Paperina', 23, 'F', 'Physics')
myself.printInfo(), rightself.printInfo(), leftself.printInfo()

# Given is the class Animal. For each task, test your changes!
# Create two realistic instances of Animals
# Print the name of each object
# Change the amount of legs of one object using the dot notation 
# Add a method setLegs() to set the legs of an object and repeat task 3 but this time using the method.
# Add a method getLegs() to return the amount of legs
# Add a method named printInfo that prints all attributes of the Animal
    
class Animal:
    def __init__(self, name, species, legs):
        self.name=name
        self.species=species
        self.legs=legs
    def setLegs(self, legs):
        self.legs=legs
    def getLegs(self):
        return self.legs
    def printInfo(self):
        print(self.name, self.species, self.legs)

cat, dog=Animal('Whiskers', 'cat', 4), Animal('Snoopy', 'dog', 4)
dog.setLegs(3)
print(dog.getLegs(), cat.getLegs())
dog.printInfo(), cat.printInfo()

# Write a new class called Food, it should have name, price and description as attributes.
# Instantiate at least three different foods you know and like.
# Create a new class called Menu, it should have a list (of Foods) as attribute. __init__ should take a list of Foods as optional parameters (default=[])
# Create a addFood() and removeFood() for the Menu
# Create a few new Food instances. Add each to the Menu using the respective Method.
# Add a method printPrices() that list all items on the Menu with their prices.
# Add a Menu method getAveragePrice() that returns the average Food price of the Menu
    
class Food:
    def __init__(self, name, price, description):
        self.name=name
        self.price=price
        self.description=description

class Menu:
    def __init__(self, foods=[]):
        self.foods=foods
    def addFood(self, food):
        self.foods.append(food)
    def removeFood(self, food):
        del self.foods[self.foods.index(food)]
    def printPrices(self):
        for food in self.foods:
            print(self.name, self.price)
    def getAveragePrice(self):
        return sum([food.price for food in self.foods])/len(self.foods)

pizza, kebab, risotto=Food('pizza', 8, 'tomato sauce and mozzarella'), Food('kebab', 5, 'pita bread and cow meat'), Food('risotto alla milanese', 8, 'rice, saffron cream and parmesan')
menu=Menu([pizza, kebab, risotto])
menu.addFood(Food('pasta amatriciana', 8, 'pasta with tomato sauce and pork jowls'))
menu.removeFood(pizza)
print(menu.getAveragePrice())