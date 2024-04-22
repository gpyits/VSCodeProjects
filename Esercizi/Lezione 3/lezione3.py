# 4-1. Pizzas: 
#      Think of at least three kinds of your favorite pizza. 
#      Store these pizza names in a list, and then use a for loop to print the name of each pizza:
#
#       • Modify your for loop to print a sentence using the name of the pizza, 
#         instead of printing just the name of the pizza. For each pizza, you should have 
#         one line of output containing a simple statement like I like pepperoni pizza.
#       • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#         The output should consist of three or more lines about the kinds of pizza 
#         you like and then an additional sentence, such as I really love pizza!
pizzas=['margherita', 'boscaiola', 'ortolana']
for pizza in pizzas:
    print(pizza, f'i like {pizza}!')
print('I like pizza')


# 4-2. Animals: 
#      Think of at least three different animals that have a common characteristic. 
#      Store the names of these animals in a list, and then use a for loop to print out the name of each animal:
#          
#       • Modify your program to print a statement about each animal, such as A dog would make a great pet.
#       • Add a line at the end of your program, stating what these animals have in common. 
#         You could print a sentence, such as Any of these animals would make a great pet!
pets=['dog', 'cat', 'mouse']
for pet in pets:
    print(pet, f'A {pet} would be great')
print('The car is under the table') 


# 4-3. Counting to Twenty: 
#      Use a for loop to print the numbers from 1 to 20, inclusive.
for r in range(21):
    print(r)


# 4-4. One Million: 
#      Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#      (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
'''commented for obvious reasons
numbers=[r for r in range(0, (10**6)+1)]
for number in numbers:
    print(number)
'''

# 4-5. Summing a Million: 
#      Make a list of the numbers from one to one million, and then use min() and max() 
#      to make sure your list actually starts at one and ends at one million. 
#      Also, use the sum() function to see how quickly Python can add a million numbers.
'''same thing
numbers=[r for r in range(1, (10**6)+1)]
print(min(numbers), max(numbers), sum(numbers))
'''

# 4-6. Odd Numbers: 
#      Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#      Use a for loop to print each number.
'''print(*range(1, 20, 2))'''
for i in range(1, 20, 2):
    print(i)


# 4-7. Threes: 
#      Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
mults=[i for i in range(3, 31) if i%3==0]
print(*mults)


# 4-8. Cubes: 
#      A number raised to the third power is called a cube. For example, the cube of 2 is 
#      written as 2**3 in Python. Make a list of the first 10 cubes 
#      (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
mults=[]
for i in range(1, 11):
    mults.append(i**3)
print(mults)


# 4-9. Cube Comprehension: 
#      Use a list comprehension to generate a list of the first 10 cubes.
mults=[i**3 for i in range(1, 11)]
print(*mults)

# 4-10. Slices: 
#       Using one of the programs you wrote in this chapter, add several lines to the 
#       end of the program that do the following:
#
#        • Print the message 'The first three items in the list are:'
#          Then use a slice to print the first three items from that program’s list.
#        • Print the message 'Three items from the middle of the list are:'
#          Then use a slice to print three items from the middle of the list.
#        • Print the message 'The last three items in the list are:'
#          Then use a slice to print the last three items in the list.
pizzas=['margherita', 'boscaiola', 'ortolana', 'diavola', 'quattro formaggi']
print(f'The first three items in the list are:', *pizzas[:3], 
      f'\nThree items at the middle of the list are:', *pizzas[(len(pizzas)//2)-1:(len(pizzas)//2)+2],
      f'\nThe first three items in the list are:', *pizzas[-3:])


# 4-11. My Pizzas, Your Pizzas: 
#       Start with your program from Exercise 4-1. Make a copy of the list of pizzas, 
#       and call it friend_pizzas. Then, do the following:
#
#        • Add a new pizza to the original list.
#        • Add a different pizza to the list friend_pizzas.
#        • Prove that you have two separate lists. Print the message 'My favorite pizzas are:'
#          and then use a for loop to print the first list. Print the message 'My friend’s favorite pizzas are:'
#          and then use a for loop to print the second list. Make sure each new pizza is 
#          stored in the appropriate list.
pizzas=['margherita', 'boscaiola', 'ortolana', 'diavola']
friend_pizzas=pizzas[:-1]
friend_pizzas.append('quattro formaggi')
print(pizzas, friend_pizzas)
print('My favorite pizzas are: ', *pizzas)
print('My friend\'s favorite pizzas are: ', *friend_pizzas)


# 4-12. More Loops: 
#       All versions of foods.py in this section have avoided using for loops when printing, 
#       to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
pizzas=['margherita', 'boscaiola', 'ortolana', 'diavola']
friend_pizzas=pizzas[:-1]
friend_pizzas.append('quattro formaggi')
print(pizzas, friend_pizzas)
print('My favorite pizzas are:')
for pizza in pizzas:
    print(f'{pizza}')
print('\nMy favorite friend\'s pizzas are:')
for pizza in friend_pizzas:
    print(f'{pizza}')   


# 4-14. PEP 8: 
#       Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. 
#       You won’t use much of it now, but it might be interesting to skim through it.
pass


# 4-15. Code Review: 
#       Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
#start by creating empty list
multiples=[]
#loop through 1 to 10
for number in range(1, 11):
    #append the cubed range values to the list
    multiples.append(number**3)
#print call
print(mults)


# 5-1. Conditional Tests: 
#      Write a series of conditional tests. Print a statement
#      describing each test and your prediction for the results of each test. 
#      Your code should look something like this:
#           car = 'subaru'
#           print("Is car == 'subaru'? I predict True.")
#           print(car == 'subaru')
#           print("\nIs car == 'audi'? I predict False.")
#           print(car == 'audi')
#
#       • Look closely at your results, and make sure you understand why each line
#         evaluates to True or False.
#       • Create at least 10 tests. Have at least 5 tests evaluate to True and another
#         5 tests evaluate to False.
#1 
pizza='margherita'
print("Is your favorite pizza 'margherita'? I predict False.")
print(pizza == 'margherita')
print("Is your favorite pizza 'boscaiola'? I predict False.")
print(pizza == 'boscaiola')
    
#2
car='lamborghini'
print("Is your favorite car 'ferrari'? I predict False.")
print(car == 'ferrari')
print("Is your favorite car 'lamborghini'? I predict True.")
print(car == 'lamborghini')

#3
videogame='dark souls'
print("Is your favorite videogame 'dark souls'? I predict True.")
print(videogame == 'dark souls')
print("Is your favorite vidoegame 'cuphead'? I predict False.")
print(videogame == 'cuphead')

#4
phone_brand='android'
print("Is your favorite phone brand 'android'? I predict True.")
print(phone_brand == 'android')
print("Is your favorite phone brand 'apple'? I predict False.")
print(phone_brand == 'apple')

#5
gpu_brand='nvidia'
print("Is your favorite gpu brand 'nvidia'? I predict True.")
print(gpu_brand == 'nvidia')
print("Is your favorite gpu brand 'amd'? I predict False.")
print(gpu_brand == 'amd')

# 5-2. More Conditional Tests: 
#      You don’t have to limit the number of tests you create to 10. 
#      If you want to try more comparisons, write more tests and add them to conditional_tests.py.
#      Have at least one True and one False result for each of the following:
#
#       • Tests for equality and inequality with strings
#       • Tests using the lower() method
#       • Numerical tests involving equality and inequality, greater than and less than, 
#         greater than or equal to, and less than or equal to
#       • Tests using the AND keyword and the OR keyword
#       • Test whether an item is in a list
#       • Test whether an item is not in a list
print(
    #true, false
    'piPPo'.lower()=='PIppO'.lower(), 'piPPo'.lower()=='PIpp0'.lower(), '\n',
    'pipPo'.lower()!='pLuto'.lower(), 'pipPo'.lower()!='pippo'.lower(), '\n',
    23==23, 23==24, '\n',
    23!=42, 23!=23, '\n',
    23>12, 23>42, '\n',
    23<42, 23<12, '\n',
    23>=23, 23>=42, '\n',
    23<=23, 23<=12, '\n',
    bool(1 and 1), bool(0 and 1), '\n',
    bool(0 or 1), bool(0 or 0), '\n',
    'a' in ['a', 'b', 'c'], 'd' in ['a', 'b', 'c'], '\n',
    3 not in ['a', 'b', 'c'], 'b' not in ['a', 'b', 'c']
)


# 5-3. Alien Colors #1: 
#      Imagine an alien was just shot down in a game. Create a variable called alien_color and
#      assign it a value of 'green', 'yellow', or 'red':
#
#       • Write an if statement to test whether the alien’s color is green. 
#         If it is, print a message that the player just earned 5 points.
#       • Write one version of this program that passes the if test and another that fails. 
#         (The version that fails will have no output.)
#5 points
alien_color='green'
if alien_color=='green':
    print('+5 points')
else:
    pass
#pass
alien_color='red'
if alien_color=='green':
    print('+5 points')
else:
    pass


# 5-4. Alien Colors #2: 
#      Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain:
#       • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#       • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#       • Write one version of this program that runs the if block and another that runs the else block.
#else
alien_color='red'
if alien_color=='green':
    print('+5 points')
else:
    print('+10 points')
#if
alien_color='green'
if alien_color=='green':
    print('+5 points')
else:
    print('+10 points')


# 5-5. Alien Colors #3: 
#      Turn your if-else chain from Exercise 5-4 into an if-elif-else chain:
#
#       • If the alien is green, print a message that the player earned 5 points.
#       • If the alien is yellow, print a message that the player earned 10 points.
#       • If the alien is red, print a message that the player earned 15 points.
#       • Write three versions of this program, making sure each message is printed for the appropriate color alien.
#green
alien_color='green'
if alien_color=='green':
    print('+5 points')
elif alien_color=='yellow':
    print('+10 points')
else:
    print('+15 points')

#yellow
alien_color='yellow'
if alien_color=='green':
    print('+5 points')
elif alien_color=='yellow':
    print('+10 points')
else:
    print('+15 points')

#red
    alien_color='red'
if alien_color=='green':
    print('+5 points')
elif alien_color=='yellow':
    print('+10 points')
else:
    print('+15 points')


# 5-6. Stages of Life: 
#      Write an if-elif-else chain that determines a person’s stage of life. 
#      Set a value for the variable age, and then:
#
#       • If the person is less than 2 years old, print a message that the person is a baby.
#       • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#       • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#       • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#       • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#       • If the person is age 65 or older, print a message that the person is an elder.
age=20
if age<2:
    print('baby')
elif 2<=age<4:
    print('toddler')
elif 4<=age<13:
    print('kid')
elif 13<=age<20:
    print('teenager')
elif 20<=age<65:
    print('adult')
else:
    print('elder')


# 5-7. Favorite Fruit: 
#      Make a list of your favorite fruits, and then write a series of 
#      independent if statements that check for certain fruits in your list:
#
#       • Make a list of your three favorite fruits and call it favorite_fruits.
#       • Write five if statements. Each should check whether a certain kind of 
#         fruit is in your list. If the fruit is in your list, the if block should 
#         print a statement, such as You really like Apples!
favorite_fruits=['apple', 'pear', 'strawberry', 'banana', 'blackberries']
if 'apple' in favorite_fruits:
    print('you like apples')
elif 'pear' in favorite_fruits:
    print('you like pears')
elif 'strawberry' in favorite_fruits:
    print('you like strawberries')
elif 'banana' in favorite_fruits:
    print('you like bananas')
elif 'blackberries' in favorite_fruits:
    print('you like blackberries')


# 5-8. Hello Admin: 
#      Make a list of five or more usernames, including the name 'admin'. 
#      Imagine you are writing code that will print a greeting to each user after 
#      they log in to a website. Loop through the list, and print a greeting to each user:
#
#       • If the username is 'admin', print a special greeting, such as 'Hello admin, would you 
#         like to see a status report?'
#       • Otherwise, print a generic greeting, such as 'Hello Jaden, thank you for logging in again.'
for user in ['admin', 'pippo', 'pluto', 'paperino', 'minnie']:
    if user=='admin':
        print('Hi admin, I\'m dad')
    else:
        print(f'Hello {user}')


# 5-9. No Users: 
#      Add an if test to hello_admin.py to make sure the list of users is not empty:
#
#       • If the list is empty, print the message We need to find some users!
#       • Remove all of the usernames from your list, and make sure the correct message is printed.
users=[]
for user in users:
    if users==[]:
        print('We need to find some users!')
    elif user=='admin':
        print('Hi admin, I\'m dad')
    else:
        print(f'Hello {user}')


# 5-10. Checking Usernames: 
#       Do the following to create a program that simulates how websites ensure that everyone has a unique username:
#
#       • Make a list of five or more usernames called current_users.
#       • Make another list of five usernames called new_users. 
#         Make sure one or two of the new usernames are also in the current_users list.
#       • Loop through the new_users list to see if each new username has already been used. 
#         If it has, print a message that the person will need to enter a new username. 
#         If a username has not been used, print a message saying that the username is available.
#       • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
#         (To do this, you’ll need to make a copy of current_users containing the lowercase 
#          versions of all existing users.)
current_users=['topolino', 'pippo', 'pluto', 'paperino', 'minnie']
new_users=['paperoga', 'topolino', 'pluto', 'gastone', 'nonna papera']
for name in new_users:
    if name.lower() in [i.lower() for i in current_users]:
        print(f'{name} was taken, insert new username')
    else: 
        print(f'{name} is available, welcome')


# 5-11. Ordinal Numbers: 
#       Ordinal numbers indicate their position in a list, such as 1st or 2nd.
#       Most ordinal numbers end in th, except 1, 2, and 3:
#
#       • Store the numbers 1 through 9 in a list.
#       • Loop through the list.
#       • Use an if-elif-else chain inside the loop to print the proper 
#         ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
#         and each result should be on a separate line.
numbers=[str(i) for i in range(1, 10)]
for r in range(len(numbers)):
    if r==0:
        numbers[r]+='st'
        numbers[r+1]+='nd'
        numbers[r+2]+='nd'
    elif r==1 or r==2:
        continue
    else:
        numbers[r]+='th'
print(numbers)