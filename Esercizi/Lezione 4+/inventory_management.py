# Create a function that defines an item with a code, name, quantity, and price.
# Create a database or dictionary to store the items in inventory.
# Implement functions to add, remove, search, and update items in the inventory.
# Use for loops and conditional statements to manage the various inventory operations.

#creates item, capitalizes first letter of each name for convenience
def item(name, code, quantity, price) ->list:
    return [name[0].upper()+name[1:].lower(), code, quantity, price]

#creates inventory dictionary
def inventory_maker(*args):
    inventory={}
    for arg in args:
        inventory[arg[0]]=[arg[1], arg[2], arg[3]]
    return inventory

#adds item to inventory
def add(inventory, item):
    inventory[item[0][0].upper()+item[0][1:].lower()]=[item[1], item[2], item[3]]
    return inventory

#removes item from inventory
def remove(inventory, item_name: str):
    del inventory[item_name[0].upper()+item_name[1:].lower()]
    return inventory

#searches for items in inventory
def search(inventory, item_name: str):
    item_name=item_name[0].upper()+item_name[1:].lower()
    if item_name in inventory.keys():
        print(f'Found item {item_name} in inventory')
        return True
    else:
        print('Your search does not match any inventory items')
        return False

def update(inventory, item, name=None, code=None, quantity=None, price=None):
    pass

inventory=inventory_maker(item('Phone', 0, 2, 30), item('Car', 1, 1, 30000))
add(inventory, item('apple', 4, 10, 1))
remove(inventory, 'apple')
search(inventory, 'phone')
print(inventory)