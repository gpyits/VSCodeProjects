class Zoo:
    '''Creates Zoo object. Can print information about the Zoo itself.'''
    def __init__(self, fences: list=[], zoo_keepers: list=[]) -> None:
        self.fences: list[Fence]=fences
        self.zoo_keepers: list[ZooKeeper]=zoo_keepers
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

class Animal:
    '''Creates animal object'''
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.name: str=name
        self.species: str=species
        self.age: int=age
        self.height: float=height
        self.width: float=width
        self.area: float=height*width
        self.preferred_habitat: str=preferred_habitat
        self.fence: Fence=None
        self.health: int=round(100*(1/age), 3)
        if height<=0 or width<=0 or age<=0:
            raise Exception(f'Error: height, weight or age cannot be zero or lower. Animal object "{name}" was not created')         

class Fence:
    '''Creates Fence object'''
    def __init__(self, area: int, temperature: float, habitat: str, animals: list[Animal]=[]) -> None:
        self.temperature: float=temperature
        self.habitat: str=habitat
        self.animals: list[Animal]=list(set([animal for animal in animals if animal.preferred_habitat==self.habitat]))
        self.area: int=area-sum([animal.area for animal in self.animals])
        if self.area<0:
            raise Exception(f'Error: total animal area exceeds fence capacity. Fence object was not created')
        for animal in self.animals:
            animal.fence=self

class ZooKeeper:
    '''Creates ZooKeeper object. Can perform various operations in the zoo such as adding, removing animals and cleaning fences.'''
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str=name
        self.surname: str=surname
        self.id: str=id
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        if fence.habitat==animal.preferred_habitat and fence.area-(animal.height*animal.width)>=0 and animal.fence==None:
            fence.animals.append(animal)
            animal.fence=fence
            animal.fence.area-=animal.area
            print(f'Successfully added animal {animal.name} to fence')
        else:
            print(f'Error: animal {animal.name} could not be added')
    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal in fence.animals:
            fence.animals.remove(animal)
            animal.fence=None
            fence.area+=animal.area
            print(f'Successfully removed animal {animal.name} from fence')
        else:
            print(f'Error: animal {animal.name} could not be removed')
    def feed(self, animal: Animal) -> None:
        if animal.fence:
            if animal.fence.area-(animal.height*animal.width)*0.02>=0:
                animal.fence.area-=(animal.height*animal.width)*0.02
            else:
                print(f'Couldn\'t feed animal {animal.name}')
                return
        animal.area+=(animal.height*animal.width)*0.02
        animal.height+=animal.height*0.02
        animal.width+=animal.width*0.02
        animal.health+=animal.health*0.01
        print(f'Successfully fed animal {animal.name}')
    def clean(self, fence: Fence) -> float:
        occupied_area: float=sum([animal.area for animal in fence.animals])
        return occupied_area if fence.area==0 else occupied_area/fence.area