# 8-1. Message:
#      Write a function called display_message() that prints one sentence telling everyone 
#      what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
def display_message():
    return 'Learning functions'
print(display_message())

# 8-2. Favorite Book: 
#      Write a function called favorite_book() that accepts one parameter, title. 
#      The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
#      Call the function, making sure to include a book title as an argument in the function call.
def favorite_book(title):
    return f'One of my favorite books is {title}'
print(favorite_book('A Little Life'))


# 8-3. T-Shirt: 
#      Write a function called make_shirt() that accepts a size and the text of a message 
#      that should be printed on the shirt. The function should print a sentence summarizing 
#      the size of the shirt and the message printed on it. Call the function once using positional 
#      arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size: str, text):
    return size, text
print(make_shirt('large', 'lorem ipsum'))


# 8-4. Large Shirts: 
#      Modify the make_shirt() function so that shirts are large by default with a message
#      that reads 'I love Python'. Make a large shirt and a medium shirt with the default message, 
#      and a shirt of any size with a different message.
def make_shirt(size='large', text='I love Python'):
    return size, text
print(make_shirt())
print(make_shirt(size='medium'))


# 8-5. Cities: 
#      Write a function called describe_city() that accepts the name of a city and its country. 
#      The function should print a simple sentence, such as Reykjavik is in Iceland. 
#      Give the parameter for the country a default value. Call your function for three different cities, 
#      at least one of which is not in the default country.
def describe_city(city, country='Italy'):
    return f'{city} is in {country}'
print(describe_city('Rome'))
print(describe_city('Milan'))
print(describe_city('Madrid', country='Spain'))


# 8-6. City Names: 
#      Write a function called city_country() that takes in the name of a city and its country. 
#      The function should return a string formatted like this: "Santiago, Chile". 
#      Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city, country):
    return f'{city}, {country}'
print(describe_city('Rome', 'Italy'))
print(describe_city('San Diego', 'California'))
print(describe_city('Sao Paulo', 'Brasil'))


# 8-7. Album:
#      Write a function called make_album() that builds a dictionary describing a music album. 
#      The function should take in an artist name and an album title, and it should return a 
#      dictionary containing these two pieces of information. Use the function to make three 
#      dictionaries representing different albums. Print each return value to show that the  
#      dictionaries are storing the album information correctly. Use None to add an optional 
#      parameter to make_album() that allows you to store the number of songs on an album. 
#      If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
#      Make at least one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title, album_songs: int=None):
    if album_songs!=None:
        return {artist_name:[album_title, album_songs]}
    return {artist_name:album_title}
dict1=make_album('Rolling Stones', 'Aftermath')
dict2=make_album('Eminem', 'Marshall Mathers LP')
dict3=make_album('MFDOOM','Madvillainy')
dict4=make_album('King Crimson', 'In The Court of the Crimson King', 5)
print(dict1, dict2, dict3, dict4)


# 8-8. User Albums: 
#      Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s 
#      artist and title. Once you have that information, call make_album() with the user’s input and print 
#      the dictionary that’s created. Be sure to include a quit value in the while loop.
# def make_album(artist_name: str=None, album_title: str=None, album_songs: int=None):
#     while artist_name==None or album_title==None or album_songs==None:
#         artist_name=input('Insert album name: ')
#         album_title=input('Insert album title: ')
#         album_songs=int(input('Insert album songs: '))
#     dictionary={}
#     dictionary[artist_name]=album_title
#     if album_songs!=None:
#         dictionary[artist_name]=[album_title, album_songs]
#     return dictionary
# print(make_album())


# 8-9. Messages: 
#      Make a list containing a series of short text messages. Pass the list to a function called 
#      show_messages(), which prints each text message.
messages=['I love Python', 'lorem ipsum dolor sit amet', 'You\'ve met with a terrible fate']
def show_messages(messages):
    for message in messages:
        print(message)
show_messages(messages)


# 8-10. Sending Messages: 
#       Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
#       that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
#       After calling the function, print both of your lists to make sure the messages were moved correctly.
messages=['I love Python', 'lorem ipsum dolor sit amet', 'I looove pizza']
def send_messages(messages):
    sent_messages=[]
    while messages!=[]:
        print(messages[0])
        sent_messages.append(messages[0])
        messages=messages[1:]
    else:
        return sent_messages
sent_messages=send_messages(messages)
print(sent_messages)


# 8-11. Archived Messages: 
#       Start with your work from Exercise 8-10. Call the function send_messages() with a copy
#       of the list of messages. After calling the function, print both of your lists to show that the original
#       list has retained its messages.
messages=['I love Python', 'lorem ipsum dolor sit amet', 'I looove pizza']
sent_messages=send_messages(messages[:])
print(messages, sent_messages)


# 8-12. Sandwiches: 
#       Write a function that accepts a list of items a person wants on a sandwich. 
#       The function should have one parameter that collects as many items as the function call provides, 
#       and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
#       using a different number of arguments each time.
def sandwich_maker(sandwich: list):
    for ingredient in sandwich:
        print(ingredient, end=' ')
sandwich_maker(['lettuce', 'tomatoes', 'meat','bread\n'])


# 8-13. User Profile: 
#       Build a profile of yourself by calling build_profile(), using your first and last names and three 
#       other key-value pairs that describe you. All the values must be passed to the function as parameters. 
#       The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67".
def build_profile(first_name, last_name, age, hair_color, weight_kg):
    return f'{first_name} {last_name}, age {age}, hair {hair_color}, weight {weight_kg}kg'


# 8-14. Cars: 
#       Write a function that stores information about a car in a dictionary. The function should 
#       always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
#       Call the function with the required information and two other name-value pairs, such as a color or an optional 
#       feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', 
#       tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 
def make_car(manufacturer, model_name, **kwargs):
    car={manufacturer:model_name}
    for key, value in kwargs.items():
        car[key]=value
    return car
print(make_car('subaru', 'outback', color='blue', tow_package=True))


# 8-15. Printing Models: 
#       Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#       Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
import carmaker as c
car=c.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


# 8-16. Imports: 
#       Using a program you wrote that has one function in it, store that function in a separate file. 
#       Import the function into your main program file, and call the function using each of these approaches:
#           import module_name
#           from module_name import function_name
#           from module_name import function_name as fn
#           import module_name as mn
#           from module_name import *
import carmaker
carmaker.make_car('subaru', 'outback', color='blue', tow_package=True)
from carmaker import make_car
make_car('subaru', 'outback', color='blue', tow_package=True)
from carmaker import make_car as mc
mc('subaru', 'outback', color='blue', tow_package=True)
import carmaker as c
c.make_car('subaru', 'outback', color='blue', tow_package=True)
from carmaker import *
carmaker.make_car('subaru', 'outback', color='blue', tow_package=True)


# 8-17. Styling Functions: 
#       Choose any three programs you wrote for this chapter, and make sure they follow the styling 
#       guidelines described in this section.
#8-9 PEP 8
messages=['I love Python', 'lorem ipsum dolor sit amet', 'You\'ve met with a terrible fate']
def show_messages(messages):
    for message in messages:
        print(message)
show_messages(messages)

#8-7 PEP 8
def make_album(artist_name, album_title, album_songs: int=None):
    if album_songs!=None:
        return {artist_name:[album_title, album_songs]}
    return {artist_name:album_title}
album_1=make_album('Rolling Stones', 'Aftermath')
album_2=make_album('Eminem', 'Marshall Mathers LP')
album_3=make_album('MFDOOM','Madvillainy')
album_4=make_album('King Crimson', 'In The Court of the Crimson King', 5)
print(album_1, album_2, album_3, album_4)

#8-3 PEP 8
def make_shirt(size: str, text):
    return size, text
print(make_shirt('large', 'I love Python!'))