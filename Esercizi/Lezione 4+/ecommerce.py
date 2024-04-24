'''
Create a function that defines a product with a name, price, and quantity.
Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
The function should calculate the cart total and apply any discounts or taxes.
Implement a for loop to iterate over the items in the cart and print detailed 
information about each product and the total.
'''
#creates product
def product(name: str, price: int, quantity: int) ->tuple:
    return name, price, quantity

#handles taxes, discounts and viewing items
def product_viewer(product, taxes, discount=None):
    name, price, quantity=product
    discount=(discount*price)/100 if discount else 0
    taxes=(taxes*(price-discount))/100
    print(f'Viewing item: {name}\n\
            Price: {price}\n\
            Price after discount: {price-discount}\n\
            Price after taxes: {price+taxes}\n\
            Quantity: {quantity}\n\
            Total price before taxes: {(price-discount)*quantity}\n\
            Total price after taxes: {(price-discount+taxes)*quantity}')

#handles add, remove and view functions, in addition to merging product and product_viewer
def shopping_cart(taxes: int, discount: int=None, *args, add: tuple=None, remove: tuple=None, view: tuple=None):
    cart=[i for i in args]
    #add function
    if add:
        cart.append(add), print(f'Added item {add}\n\n')
    #remove function
    elif remove:
        print(f'Removed item {cart.pop(remove)[0]}\n\n')
    #view function
    elif view in cart:
        product_viewer(view, taxes, discount)
    #cart viewer
    for product in cart:
        product_viewer(product, taxes, discount)

shopping_cart(11, 10, product('Phone', 100, 2), product('Apple', 2, 10))