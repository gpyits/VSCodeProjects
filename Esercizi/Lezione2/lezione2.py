# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#      Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name='Pippo'
print(f"Hello {name}, would you like to learn some Python today?")


# 2-4. Name Cases: Use a variable to represent a person’s name, and then 
#      print that person’s name in lowercase, uppercase, and title case.
name='Pippo'
print(name.lower(), name.upper(), name.title())


# 2-5. Famous Quote: Find a quote from a famous person you admire. 
#      Print the quote and the name of its author. Your output should look something like the following, 
#      including the quotation marks: Albert Einstein once said, 
#      “A person who never made a mistake never tried anything new.”
print('Albert Camus once said, "One must imagine Sisyphus happy"')


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s 
#      name using a variable called famous_person. Then compose your message and represent 
#      it with a new variable called message. Print your message. 
name='Albert Camus'
quote='"One must imagine Sisyphus happy"'
print(f'{name} once said, {quote}')


# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#      Assign the value 'python_notes.txt' to a variable called filename. 
#      Then use the removesuffix() method to display the filename without the file extension, 
#      like some file browsers do.
filename='python_notes.txt'
print(filename.removesuffix('.txt'))


# 3-1. Names: Store the names of a few of your friends in a list called names. 
#      Print each person’s name by accessing each element in the list, one at a time.
friends=['Pippo', 'Pluto', 'Paperino']
for i in friends:
    print(i)


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of 
#      just printing each person’s name, print a message to them. 
#      The text of each message should be the same, but each message should be personalized with 
#      the person’s name.
friends=['Pippo', 'Pluto', 'Paperino']
for friend in friends:
    print(f'Hello {name}!')


# 3-3. Your Own List: Think of your favorite mode of transportation, 
#      such as a motorcycle or a car, and make a list that stores several examples. 
#      Use your list to print a series of statements about these items, such as 
#      “I would like to own a Honda motorcycle.”
vehicles=['car', 'motorcycle', 'train']
for vehicle in vehicles:
    print(f'I would like to own a {vehicle}')


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#      Make a list that includes at least three people you’d like to invite to dinner. 
#      Then use your list to print a message to each person, inviting them to dinner.
people=['Pippo', 'Pluto', 'Paperino']
for person in people:
    print(f'Hi {person}, you are invited to dinner')

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
#     so you need to send out a new set of invitations. You’ll have to think of someone else to invite:
#
#      • Start with your program from Exercise 3-4. Add a print() 
#        call at the end of your program, stating the name of the guest who can’t make it.
#      • Modify your list, replacing the name of the guest who can’t make it with the name of 
#        the new person you are inviting.
#      • Print a second set of invitation messages, one for each person who is still in your list.
people=['Pippo', 'Pluto', 'Paperino', 'Gastone', 'Topolino']
cant_make=people[-2:]
people=people[:-2]
people.append('Minnie', 'Nonna Papera')
for person in people:
    print(f'Hi {person}, you are invited to dinner')
for person in cant_make:
    print(f'Hi {person}, you are no longer invited to dinner')


# 3-6. More Guests - You just found a bigger dinner table, so now more space is available. 
#      Think of three more guests to invite to dinner:
#
#      • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
#        informing people that you found a bigger table.
#      • Use insert() to add one new guest to the beginning of your list.
#      • Use insert() to add one new guest to the middle of your list.
#      • Use append() to add one new guest to the end of your list.
#      • Print a new set of invitation messages, one for each person in your list.
print(f'More space available, inviting more guests')
people.insert(0, 'Francesco')
people.append('Francescodinuovo')
people.insert(len(people)//2, 'SempreFrancesco')
for person in people:
    print(f'Hi {person}, you are invited to dinner')


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in 
#      time for the dinner, and now you have space for only two guests:
#
#      • Start with your program from Exercise 3-6. Add a new line that prints a message saying 
#        that you can invite only two people for dinner.
#      • Use pop() to remove guests from your list one at a time
#        until only two names remain in your list. Each time you pop a name from your list, 
#        print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#      • Print a message to each of the two people still on your list, letting them know they’re still invited.
#      • Use del to remove the last two names from your list, so you have an empty list. 
#      Print your list to make sure you actually have an empty list at the end of your program.
print(f'Hi, only two people will be invited for dinner')
for i in range(len(people)-2):
    print(f'Sorry {people.pop(i)}, you aren\'t invited to dinner')
    people=people[::-1]
print(f'{people[0]} you are still invited', f'{people[1]} you are still invited')
del(people[0], people[0])
print(people)


# 3-8. Seeing the World - Think of at least five places in the world you’d like to visit:
#
#      • Store the locations in a list. Make sure the list is not in alphabetical order.
#      • Print your list in its original order. Don’t worry about printing the list neatly; 
#        just print it as a raw Python list.
#      • Use sorted() to print your list in alphabetical order without modifying the actual list.
#      • Show that your list is still in its original order by printing it.
#      • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#      • Show that your list is still in its original order by printing it again.
#      • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#      • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#      • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that 
#        its order has been changed.
#      • Use sort() to change your list so it’s stored in reverse-alphabetical order.
#        Print the list to show that its order has changed.
places=['Canada', 'Australia', 'Finland', 'Milan', 'Spain']
print(sorted(places))
print(places)
print(sorted(places)[::-1])
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


# 3-9. Dinner Guests - Working with one of the programs from Exercises 3, use len() to print 
#      a message indicating the number of people you’re inviting to dinner.
people=['Pippo', 'Pluto', 'Paperino', 'Gastone', 'Topolino']
print(f'I\'m inviting {len(people)} to dinner')

# 3-10. Every Function - Think of things you could store in a list. 
#       For example, you could make a list of mountains, rivers, countries, 
#       cities, languages, or anything else you’d like. Write a program that creates 
#       a list containing these items and then uses each function introduced in this chapter at least once.
#       -->pop del sorted reverse sort insert append print
objects=['Pippo', 'Pluto', 'Paperino', 'Gastone', 'Topolino']
objects.append('Malta')
objects.pop(0)
del(objects[0])
sorted(objects[i])
objects.reverse()
objects.sort()
objects.insert(0, 'aaa')
print(objects)


# 6-1. Person - Use a dictionary to store information about a person you know. 
#      Store their first name, last name, age, and the city in which they live. 
#      You should have keys such as first_name, last_name, age, and city. 
#      Print each piece of information stored in your dictionary.
info={'first_name':'Francesco', 'last_name':'Totti', 'age':'44', 'city':'Rome'}
for item in info.items():
    print(f'{item[0]}:{item[1]}')


# 6-2. Favorite Numbers - Use a dictionary to store people’s favorite numbers. 
#      Think of five names, and use them as keys in your dictionary. 
#      Think of a favorite number for each person, and store each as a value in your dictionary. 
#      Print each person’s name and their favorite number. For even more fun, 
#      poll a few friends and get some actual data for your program.
numbers={'Pippo':0, 'Pluto':1, 'Paperino':2, 'Gastone':3, 'Topolino':4}
for item in numbers.items():
    print(f'{item[0]}:{item[1]}')


# 6-3. Glossary - A Python dictionary can be used to model an actual dictionary. 
#      However, to avoid confusion, let’s call it a glossary:
#
#      • Think of five programming words you’ve learned about in the previous chapters. 
#        Use these words as the keys in your glossary, and store their meanings as values.
#      • Print each word and its meaning as neatly formatted output. 
#        You might print the word followed by a colon and then its meaning, 
#        or print the word on one line and then print its meaning indented on a second line. 
#      Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
glossary={
    'NAN':'not a number',
    'Program':'a set of instrucions', 
    'CPU':'central pprocessing unit', 
    'GPU':'graphic processing unit', 
    'RAM':'random access memory'
    }
for item in glossary.items():
    print(f'{item[0]}:\n{item[1]}\n')

# 6-7. People - Start with the program you wrote for Exercise 6-1. 
#      Make two new dictionaries representing different people, and store all three 
#      dictionaries in a list called people. Loop through your list of people. 
#      As you loop through the list, print everything you know about each person.
person1={'first_name':'Francesco', 'last_name':'Totti', 'age':'44', 'city':'Rome'}
person2={'first_name':'Cristiano', 'last_name':'Ronaldo', 'age':'39', 'city':'Mateira'}
person3={'first_name':'Lionel', 'last_name':'Messi', 'age':'36', 'city':'Rosario'}
people=[person1, person2, person3]
for person in people:
    for item in person.items():
        print(f'{item[0]}:{item[1]}')
    print('')

# 6-8. Pets - Make several dictionaries, where each dictionary represents a different pet. 
#      In each dictionary, include the kind of animal and the owner’s name. 
#      Store these dictionaries in a list called pets. Next, loop through your list and as
#      you do, print everything you know about each pet. 
pet1={'species':'dragon', 'owner_name':'Totti'}
pet2={'species':'alpaca', 'owner_name':'Berlusconi'}
pet3={'species':'mouse', 'owner_name':'Angelo'}
pets=[pet1, pet2, pet3]
for pet in pets:
    for item in pet.items():
        print(f'{item[0]}:{item[1]}')
    print('')


# 6-9. Favorite Places - Make a dictionary called favorite_places. 
#      Think of three names to use as keys in the dictionary, and store one to three 
#      favorite places for each person. To make this exercise a bit more interesting, 
#      ask some friends to name a few of their favorite places. 
#      Loop through the dictionary, and print each person’s name and their favorite places.
favorite_places={'Totti':['Rome', 'lorem'], 'Ronaldo':'Mateira', 'Messi':['Rosario', 'ipsum']}
for item in favorite_places.items():
    print(f'{item[0]}:\n{item[1]}\n')


# 6-10. Favorite Numbers - Modify your program from Exercise 6-2 so each person can have 
#       more than one favorite number. Then print each person’s name along with their favorite numbers.
numbers={'Pippo':[0, 2], 'Pluto':[1, 2, 3, 4], 'Paperino':2, 'Gastone':[3, 8], 'Topolino':4}
for item in numbers.items():
    print(f'{item[0]}:{item[1]}')


# 6-11. Cities - Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#       Create a dictionary of information about each city and include the country that the city is in, 
#       its approximate population, and one fact about that city. The keys for each city’s dictionary should 
#       be something like country, population, and fact. Print the name of each city and all of the 
#       information you have stored about it.
cities={
        'Rome':['Italy', '3m people', 'colosseum'], 
        'Milan':['Italy', '1m people', 'dome'], 
        'Naples':['Italy', '3m people', 'food']
        }
for item in cities.items():
    print(f'{item[0]}:{item[1]}')


# 6-12. Extensions - We’re now working with examples that are complex enough that they can be 
#       extended in any number of ways. Use one of the example programs from this chapter, 
#       and extend it by adding new keys and values, changing the context of the program, 
#       or improving the formatting of the output.
pet1={'species':'dragon', 'owner_name':'Totti', 'pet_age':3, 'pet_name':'Puponer'}
pet2={'species':'alpaca', 'owner_name':'Berlusconi', 'pet_age':10, 'pet_name':'Orchidea'}
pet3={'species':'mouse', 'owner_name':'Angelo', 'pet_age':2000, 'pet_name':'Il'}
pets=[pet1, pet2, pet3]
for pet in pets:
    for item in pet.items():
        print(f'{item[0]}:{item[1]}')
    print('')
