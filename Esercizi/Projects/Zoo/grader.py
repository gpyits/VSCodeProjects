from Esercizi.Projects.Zoo.zoo import Animal, Fence, ZooKeeper, Zoo

score = 0

def feed_animal(keeper, animal):
    global score
    i: int = 1
    while True:
        old_area: float = animal.fence.area
        old_height, old_width = animal.height, animal.width
        keeper.feed(animal) 
        new_area = old_area + (old_height * old_width)
        new_area -= animal.height * animal.width
        
        if animal.fence.area >= ((old_height + old_height * .02) * (old_width + old_width *.02)):
            if (round(old_height + old_height * .02, 3) == round(animal.height, 3)) and (round(old_width + old_width *.02,3) == round(animal.width, 3)):
                score += 0.5
            else:
                print(f"Test {i+8} Failed: The height of {animal.name} must be {old_height + old_height * .02} and not {animal.height}"\
                    + f"; The width of {animal.name} must be {old_width + old_width *.02} and not {animal.width}")
            
            if round(new_area, 3) == round(animal.fence.area, 3):
                score += 0.5
            else:
                print(f'TEST {i+8} bis: The area of {animal.fence} must be {round(new_area,3)} and not {round(animal.fence.area,3)}')        
        else:
            break
        i += 1
        
def clean_fence(fence):
    occupied_area: float = 0
    for animal in fence.animals:
        occupied_area += animal.height * animal.width
    return occupied_area / fence.area if fence.area != 0 else occupied_area
    
def run_tests():
    global score
    # Initialize some test objects
    lion = Animal(name="Simba", species="Lion", age=5, height=1.2, width=2.0, preferred_habitat="Savannah")
    elephant = Animal(name="Dumbo", species="Elephant", age=10, height=3.0, width=4.0, preferred_habitat="Jungle")
    polar_bear = Animal(name="Snowball", species="Polar Bear", age=8, height=1.5, width=2.5, preferred_habitat="Arctic")

    fence1 = Fence(area=50, temperature=20, habitat="Savannah")
    fence2 = Fence(area=100, temperature=-5, habitat="Arctic")
    fence3 = Fence(area=100, temperature=27, habitat="Jungle")

    keeper = ZooKeeper(name="Bardh", surname="Prenkaj", id="PRNBDH95M09Z160W")

    zoo = Zoo([fence1, fence2, fence3], [keeper])

    # Test 1: Create Animals
    if lion.name == "Simba":
        score += 1
    else:
        print("Test 1 Failed: Incorrect name for Lion")
    
    if elephant.species == "Elephant":
        score += 1
    else:
        print("Test 1 Failed: Incorrect species for Elephant")
        
    if polar_bear.age == 8:
        score += 1
    else:
        print("Test 1 Failed: Incorrect age for Polar Bear")

    score /= 3

    # Test 2: Create Fences
    if fence1.area == 50:
        score += 0.5
    else:
        print("Test 2 Failed: Incorrect area for Fence 1")
        
    if fence2.temperature == -5:
        score += 0.5
    else:
        print("Test 2 Failed: Incorrect temperature for Fence 2")
    
    fence1_area: float = fence1.area
    # Test 3: Add Animals to Fences
    keeper.add_animal(lion, fence1)
    keeper.add_animal(elephant, fence1)
    keeper.add_animal(polar_bear, fence2)
    keeper.add_animal(elephant, fence3)
     
    curr_score = 0
    if len(fence1.animals) == 1:
        curr_score += 1
    else:
        print(f"Test 3 Failed: Animals not added to {fence1} correctly")
        
    if len(fence2.animals) == 1:
        curr_score += 1
    else:
        print(f"Test 3 Failed: {polar_bear} not added to {fence1} correctly")
        
    if len(fence3.animals) == 1:
        curr_score += 1
    else:
        print(f"Test 3 Failed: {elephant} not added to {fence3} correctly")
        
    print(fence1.area)
    if fence1.area == fence1_area - lion.height * lion.width:
        curr_score += 1
    else:
        print(f"TEST #3 bis: The area of {fence1} should be {fence1_area - lion.height * lion.width}")
    
    score += curr_score / 4

    old_fence1_area: float = fence1.area
    # Test 4: Remove Animals from Fences
    keeper.remove_animal(lion, fence1)
    if lion not in fence1.animals:
        score += 0.5
    else:
        print(f"Test 4 Failed: {lion} not removed from {fence1} correctly")
        
    if round(fence1.area, 3) == round(old_fence1_area + lion.height * lion.width, 3):
        score += 0.5
    else:
        print(f"Test 4 Failed: The area of {fence1} should be 50")
    
    old_elephant_health: float = elephant.health
    # Test 5: Feed Animals
    keeper.feed(elephant)
    if elephant.health == old_elephant_health + old_elephant_health * .01:
        score += 1
    else:
        print(f"Test 5 Failed: {elephant} must have a health of {old_elephant_health + old_elephant_health * .01}") # Growth factor of 0.02

    # Test 7: Check if Animals are Described Correctly
    print(str(elephant))
    if str(elephant) == "Animal(name=Dumbo, species=Elephant, age=10, height=3.06, width=4.08, preferred_habitat=Jungle, health=10.2)":
        score += 1
    else:
        f'Test 6 Failed: {elephant}'
    
    # Test 8: Check if Fences are Described Correctly
    if str(fence3) == "Fence(area=87.515, temperature=27, habitat=Jungle)\nwith animals:\nAnimal(name=Dumbo, species=Elephant, age=10, height=3.06, width=4.08, preferred_habitat=Jungle, health=10.1)":
        score += 1
    else:
        print(f'Test 7 Failed: {fence3}')
    
    # Test 9: Check if ZooKeepers are Described Correctly
    if str(keeper) == "ZooKeeper(name=Bardh, surname=Prenkaj, id=PRNBDH95M09Z160W)":
        score += 1
    else:
        print(f'Test 8 Failed: {keeper}')
        
    lion = Animal(name="Scar", species="Lion", age=5, height=1.2, width=2.0, preferred_habitat="Savannah")
    keeper.add_animal(lion, fence1)
    feed_animal(keeper, lion)

    fox = Animal(name="Toledo", species="Fox", age=16, height=0.5, width=1.25, preferred_habitat="Savannah")
    keeper.add_animal(fox, fence1)
    feed_animal(keeper, fox)
    
    feed_animal(keeper, elephant)
    feed_animal(keeper, polar_bear)
    
    your_time = round(keeper.clean(fence1), 3)
    actual_time = round(clean_fence(fence1), 3)
    if your_time == actual_time:
        score += 1
    else:
        print(f'The time to clean\n {fence1}\n is {actual_time} and not {your_time}')
        
    your_time = round(keeper.clean(fence2), 3)
    actual_time = round(clean_fence(fence2), 3)
    if your_time == actual_time:
        score += 1
    else:
        print(f'The time to clean \n {fence2} \n is {actual_time} and not {your_time}')
            
    your_time = round(keeper.clean(fence3), 3)
    actual_time = round(clean_fence(fence3), 3)
    if your_time == actual_time:
        score += 1
    else:
        print(f'The time to clean \n {fence3} \n is {actual_time} and not {your_time}')
    
"""try:
    run_tests()
except Exception as e:
    print("Error: ", e)"""
run_tests()
print(f'Score = {score} / 245')
 