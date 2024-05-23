class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int=0) -> None:
        self.restaurant_name: str=restaurant_name
        self.cuisine_type: str=cuisine_type
        self.number_served: int=number_served
    def describe_restaurant(self) -> None:
        print(f'Restaurant name: {self.restaurant_name}, Cuisine: {self.cuisine_type}')
    def open_restaurant(self) -> None:
        print('The restaurant is open')
    def set_number_served(self, new_number_served: int) -> None:
        self.number_served: int=new_number_served
    def increment_number_served(self, additional_served_clients: int) -> None:
        self.number_served+=additional_served_clients