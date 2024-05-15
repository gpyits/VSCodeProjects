class Zoo:
    def __init__(self, fences: list=[], zoo_keepers: list=[]) -> None:
        self.fences=fences
        self.zoo_keepers=zoo_keepers
    def describe_zoo(self) -> None:
        print('\nGuardians:')
        for zookeeper in self.zoo_keepers: 
            print(f'ZooKeeper(name={zookeeper.name}), surname={zookeeper.surname}, id={zookeeper.id}')
        print('Fences:')
        for fence in self.fences: 
            print(f'Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})\nwith animals:')
            for animal in fence.animals:
                print(f'Animal(name={animal.name}, species={animal.species}, age={animal.age})')
            print('#'*30)

class Fence:
    def __init__(self, area: int, temperature: int, habitat: str, animals: list[object]=[]) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.animals=animals

class Animal:
    def __init__(self, name: str, species: str, age: int, height: int, width: int, preferred_habitat: str, fence: Fence=None) -> None:
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.area: int=height*width
        self.preferred_habitat=preferred_habitat
        self.fence=fence
        self.health: int=round(100 * (1 / age), 3)

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name=name
        self.surname=surname
        self.id=id
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        if fence.habitat==animal.preferred_habitat and fence.area-(animal.height*animal.width)>=0:
            fence.animals.append(animal)
            animal.fence=fence
            print(f'Successfully added animal {animal.name} to fence')
        else:
            print(f'Error: animal {animal.name} could not be added')
    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal in fence.animals:
            del fence.animals[fence.animals.index(animal)]
            fence.area-=animal.area
            print(f'Successfully removed animal {animal.name} from fence')
        else:
            print(f'Error: animal {animal.name} could not be removed')
    def feed(self, animal: Animal) -> None:
        if animal.fence and animal.fence.area-(animal.area)-((animal.area)*2/100)>=0:
            animal.fence.area-=(animal.area)+((animal.area)*2/100)
        animal.height*=2/100
        animal.width*=2/100
        print(f'Successfully fed animal {animal.name}')
    def clean(self, fence: Fence) -> int:
        total_area: int=sum([animal.area for animal in fence.animals])
        return total_area if fence.area-total_area==0 else total_area/(fence.area-total_area)