'''
Create a function that defines a product with a name, price, and quantity.
Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
The function should calculate the cart total and apply any discounts or taxes.
Implement a for loop to iterate over the items in the cart and print detailed 
information about each product and the total.
'''
def product(name: str, price: int, quantity: int):
    return (name, price, quantity)

def shopping_cart(*args, add=None, remove=None, view=None):
    cart=[i for i in args]
    discount=10
    taxes=11
    if add:
        cart.append(add)
    elif remove:
        cart.pop(remove)
    elif view in cart:
        print(view)
    #returns the generator, resolve 
    return ((i[0], (discount/i[1])*100, i[2]//taxes) for i in cart)

print(shopping_cart(product('Phone', 1, 100), product('Apple', 2, 2)))