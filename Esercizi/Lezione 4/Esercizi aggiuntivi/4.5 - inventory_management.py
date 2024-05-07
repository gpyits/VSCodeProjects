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

#adds item to inventory and returns it
def add(inventory, item):
    inventory[item[0][0].upper()+item[0][1:].lower()]=[item[1], item[2], item[3]]
    return item

#removes item from inventory and returns it
def remove(inventory, item_name: str):
    return inventory.pop(item_name[0].upper()+item_name[1:].lower(), None)

#searches for items in inventory
def search(inventory, item_name: str) -> bool:
    if item_name[0].upper()+item_name[1:].lower() in inventory.keys():
        return True
    else:
        return False

#updates specified values of inventory item and returns it
def update(inventory, item_name, name=None, code=None, quantity=None, price=None):
    item_name=item_name[0].upper()+item_name[1:].lower()
    inventory[item_name][0]=code if code!=None else inventory[item_name][0]
    inventory[item_name][1]=quantity if quantity!=None else inventory[item_name][1]
    inventory[item_name][2]=price if price!=None else inventory[item_name][2]
    if name:
        name=name[0].upper()+name[1:].lower()
        inventory[name]=inventory[item_name]
        del inventory[item_name]
        return item(name, *inventory[name])
    return item(item_name, *inventory[item_name])


inventory=inventory_maker(item(name='Phone', code=1, quantity=1, price=1))
print(add(inventory, item('apple', 4, 10, 1)))
print(remove(inventory, 'apple'))
print(search(inventory, 'phone'))
print(update(inventory, 'phone', name='laptop', code=0, quantity=0, price=0))
print(inventory)