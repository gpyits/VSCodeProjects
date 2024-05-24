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

####### LEZIONE 6 #######

# 9.1 - Restaurant: 
# Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name: str=restaurant_name
        self.cuisine_type: str=cuisine_type
    def describe_restaurant(self) -> None:
        print(f'Restaurant name: {self.restaurant_name}, Cuisine: {self.cuisine_type}')
    def open_restaurant(self) -> None:
        print('The restaurant is open')

restaurant1=Restaurant('Kirin', 'Chinese cuisine')
print(restaurant1.restaurant_name, restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# 9.2 - Three Restaurants: 
# Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call describe_restaurant() for each instance.
restaurant1=Restaurant('Kirin', 'Chinese cuisine')
restaurant2=Restaurant('Pizzeria Roma', 'Italian cuisine')
restaurant3=Restaurant('New Delhi Restaurant', 'Indian cuisine')
restaurant1.describe_restaurant(), restaurant2.describe_restaurant(), restaurant3.describe_restaurant()

# 9.3 - Users: 
# Make a class called User. 
# Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name: str, last_name: str, nickname: str, password: str, status: str='Offline') -> None:
        self._first_name: str=first_name
        self._last_name: str=last_name
        self.nickname: str=nickname
        self.__password: str= password
        self.status: str=status
    def describe_user(self) -> None:
        print(f'Nickname: {self.nickname}, Status: {self.status}')
    def greet_user(self) -> None:
        print(f'Hello {self.nickname}')

user1=User('Mario', 'Mario', 'password', 'TheGreatestPlumber')
user2=User('Luigi', 'Mario', 'qwerty123', 'GREENCAP')
user1.describe_user(), user1.greet_user()
user2.describe_user(), user2.greet_user()

# 9.4 - Number Served: 
# Start with your program from Exercise 9-1. 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again. 
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. 
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int=0) -> None:
        self.restaurant_name: str=restaurant_name
        self.cuisine_type: str=cuisine_type
        self.number_served: int=number_served
    def describe_restaurant(self) -> None:
        print(f'Restaurant name: {self.restaurant_name}, Cuisine: {self.cuisine_type}')
    def open_restaurant(self) -> None:
        print('The restaurant is open')
    def set_number_served(self, new_number_served: int) -> None:
        self.number_served: int=new_number_served
    def increment_number_served(self, additional_served_clients: int) -> None:
        self.number_served+=additional_served_clients

restaurant1=Restaurant('Kirin', 'Chinese cuisine')
print(restaurant1.number_served)
restaurant1.number_served=2
print(restaurant1.number_served)
restaurant1.set_number_served(3)
print(restaurant1.number_served)
restaurant1.increment_number_served(200)

# 9.5 - Login Attempts: 
# Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.
class User:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str=first_name
        self.last_name: str=last_name
        self.login_attempts: int=0
    def describe_user(self) -> None:
        print(f'First name: {self.first_name}, Last name: {self.last_name}')
    def greet_user(self) -> None:
        print(f'Hello {self.first_name} {self.last_name}')
    def increment_login_attempts(self, new_login_attempts: int) -> None:
        self.login_attempts+=new_login_attempts
    def reset_login_attempts(self) -> None:
        self.login_attempts=0

user1=User('Mario', 'Mario')
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

# 9.6 - Ice Cream Stand: 
# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method. 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list[str], number_served: int=0) -> None:
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors=flavors
    def print_flavors(self) -> None:
        print('Flavors:', end=' '), print(*self.flavors, sep=', ')

stand1=IceCreamStand('Gelateria', 'Ice cream', ['Vanilla', 'Chocolate', 'Strawberries'])
stand1.print_flavors()

# 9.7 - Admin: 
# An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 
class Admin(User):
    def __init__(self, first_name: str, last_name: str, privileges: list[str]=['can add post', 'can delete post', 'can ban user']) -> None:
        super().__init__(first_name, last_name)
        self.privileges: list=privileges
    def show_privileges(self) -> None:
        print('Privileges:', end=' '), print(*self.privileges, sep=', ')

admin1=Admin('Luigi', 'Mario')
admin1.show_privileges()

# 9.8 - Privileges: 
# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.
class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges=privileges
    def show_privileges(self) -> None:
        print('Privileges:', end=' '), print(*self.privileges, sep=', ')

class Admin(User):
    def __init__(self, first_name: str, last_name: str, privileges: Privileges) -> None:
        super().__init__(first_name, last_name)
        self.privileges: Privileges=privileges

privileges1=Privileges(['can add post', 'can delete post', 'can ban user'])
admin2=Admin('Mario', 'Mario', privileges1)
admin2.privileges.show_privileges()

# 9.9 - Battery Upgrade: 
# Use the final version of electric_car.py from this section. 
# Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 65 if it isn’t already. 
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
# You should see an increase in the car’s range.
pass

# 9.10 - Imported Restaurant: 
# Using your latest Restaurant class, store it in a module. 
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

'''
module stored in restaurant.py
made separate file restaurant_tester.py
'''

# 9.11. Imported Admin: 
# Start with your work from Exercise 9-8. 
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

'''
modules stored in users.py
made separate file user_tester.py
'''

# 9.12. Multiple Modules: 
# Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

'''
user module stored in user.py
privileged user modules stored in admin_user.py
tested in separate file user_tester.py
'''

# 9.13. Dice: 
# Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import random

class Die:
    def __init__(self, sides: int=6) -> None:
        self.sides: int=sides
    def roll_die(self):
        print(random.randrange(1, self.sides+1))

Die().roll_die()
for i in range(10): print('d6: ', end=' '), Die().roll_die()
for i in range(10): print('d20:', end=' '), Die(20).roll_die()

# 9.14. Lottery: 
# Make a list or tuple containing a series of 10 numbers and 5 letters. 
# Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.ù
class Lottery:
    def __init__(self, winning_sequence: tuple=(1, 2, 3, 6, 8, 'd', 'f', 'l', 's', 'g')) -> None:
        self.winning_sequence: tuple=winning_sequence
    def try_luck(self) -> None:
        if input('Try your luck\nWrite 4 characters, numbers or letters: ')==''.join(str(i) for i in random.sample(self.winning_sequence, 4)):
            print('Congratulations! You won!')
        else: print('You lose. Better luck next time!')

Lottery().try_luck()

# 9.15. Lottery Analysis: 
# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

def lottery_tester(ticket: list, winning_sequence: tuple=(1, 2, 3, 6, 8, 'd', 'f', 'l', 's', 'g')):
    tries=1
    while True:
        if ticket!=random.sample(winning_sequence, 4):
            tries+=1
        else:
            print(f'Won the lottery at try no. {tries}')
            return

lottery_tester([8, 3, 2, 'f'])