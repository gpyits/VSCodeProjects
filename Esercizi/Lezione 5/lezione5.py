# 1. Create a Playlist:
# Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
# The function should return a dictionary with the playlist name and a set of songs. 
# Call the function with different numbers of songs to demonstrate flexibility.
# Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

# Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). 
# add_like(dictionary, “Road Trip”, liked=True)
# This function should return an updated dictionary.

def create_playlist(playlist_name: str, song_titles: set) -> dict:
    return {playlist_name:song_titles}

create_playlist('Road Trip', {'Song 1', 'Song2'})
playlist=create_playlist('lorem', {'ipsum', 'dolor', 'song3', 'song4'})

def add_like(dictionary: dict, playlist_name: str, liked: bool) -> dict:
    dictionary['liked']=True
    return dictionary

add_like(playlist, 'Road Trip', liked=True)

# 2. Book Collection:
# Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
# This function should return a dictionary where the author's name is the key and the value is a list of their books. 
# Demonstrate this function by adding books for different authors.
# Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

# Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details.
# delete_book(dictionary, “Mark Twain”)
# This function should return an updated dictionary.

def add_book(author_name: str, book_titles: list) -> dict:
    return {author_name: book_titles}

author=add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

def delete_book(dictionary: dict, author_name: str) -> dict:
    dictionary.pop(author_name, None)
    return dictionary

delete_book(author, 'Mark Twain')
            
# 3. Personal Info:
# Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
# Make occupation, location, and age optional parameters. 
# Use this function to create profiles for different people, demonstrating how it handles these optional parameters.
# Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)

def build_profile(name: str, surname: str, occupation: str=None, location: str=None, age: int=None) -> dict:
    result={'name':name, 'surname':surname, 'occupation':occupation if occupation else None, 'location':location if location else None, 'age':age if age else None}
    return {k:v for k, v in result.items() if v!=None} 

build_profile("John", "Doe")

# 4. Event Organizer:
# Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
# The function should return a dictionary that includes the event name and a list of the participants. 
# Call this function with varying numbers of participants to plan different events.
# Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

# Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.
# modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)

def plan_event(name: str, participants_list: list, hour: str) -> dict:
    return {'event name': name, 'participants': participants_list, 'hour':hour}

event=plan_event("Code Workshop", ["Alice", "Bob", "Charlie"], '4pm')

def modify_event(dictionary: dict, new_name: str=None, new_participants_list: list=None, new_hour: str=None) -> dict:
    dictionary['event name']=new_name if new_name else dictionary['event name']
    dictionary['participants']=new_participants_list if new_participants_list else dictionary['participants']
    dictionary['hour']=new_hour if new_hour else dictionary['hour']
    return dictionary

event=modify_event(event, new_name='event', new_hour='5pm')

# 5. Shopping List:
# Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. 
#It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.
# Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

# Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.
# print_shopping_list(dictionary, "Grocery Store")

def create_shopping_list(store_name: str, items: set):
    return {store_name:items}

store=create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

def print_shopping_list(dictionary: dict, store_name: str) -> None:
    print(*dictionary[store_name])

print_shopping_list(store, "Grocery Store")