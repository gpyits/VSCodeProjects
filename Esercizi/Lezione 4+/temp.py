#snippet tester
def product(name, price, quantity):
    return name, price, quantity

def product_viewer(product, taxes, discount=0):
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

def cart(taxes, discount, *args, add=None, remove=None, view=None):
    # for product in args:
    #     product_viewer(product, taxes, discount)
    if view in args:
        product_viewer(view, taxes, discount)
        # name, price, quantity = product
        # print(f'name: {name}\nprice: {price}\nquantity: {quantity}\n')

cart(11, 0, product('leonardo', 100, 2), product('giuseppe', 100, 1), view=('leonardo', 100, 2))