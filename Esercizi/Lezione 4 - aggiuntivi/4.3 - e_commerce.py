'''
Create a function that defines a product with a name, price, and quantity.
Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
The function should calculate the cart total and apply any discounts or taxes.
Implement a for loop to iterate over the items in the cart and print detailed 
information about each product and the total.
'''
#creates product
def product(name: str, price: float, quantity: int) ->tuple:
    return name, price, quantity

#handles taxes, discounts and viewing items
def product_viewer(product, taxes, discount=0):
    name, price, quantity=product
    discount=(discount*price)/100 if discount else 0
    taxes=(taxes*(price-discount))/100
    print(f'Viewing item: {name}\n\
            Price: {price}$\n\
            Price after discount: {price-discount}$\n\
            Price after taxes: {price+taxes}$\n\
            Quantity: {quantity}\n\
            Total price before taxes: {(price-discount)*quantity}$\n\
            Total price after taxes: {(price+taxes)*quantity}$\n')
    return (price+taxes)*quantity

#handles add, remove and view functions, in addition to merging product and product_viewer
def shopping_cart(taxes: int, discount: int, *args, add: tuple=None, remove: tuple=None, view: tuple=None):
    total_price=[]
    cart=[*args]
    #add function
    if add:
        cart.append(add), print(f'Added item {add[0]}\n')
    #remove function
    if remove:
        cart.remove(remove), print(f'Removed item {remove[0]}\n')
    #view function
    if view in cart:
        product_viewer(view, taxes, discount)
    #cart viewer
    for product in cart:
        total_price.append(product_viewer(product, taxes, discount))
    print(f'Total price of items: {sum(total_price)}$')
    return cart

shopping_cart(11, 50, product('Phone', 300, 2), product('Apple', 0.50, 3), add=product('Fridge', 800, 1), remove=product('Phone', 300, 2), view=product('Fridge', 800, 1))