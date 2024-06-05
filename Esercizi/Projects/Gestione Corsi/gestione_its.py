# ### Classe Building:
# La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

# ### Classi Person, Student e Lecturer:
# La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
# Le classi Student e Lecturer ereditano da Person.
# Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
#     - set_group(group): Associa un gruppo di studio allo studente

# ### Classe Group:
# La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
# - Metodi:
#     - get_name(): Restituisce il nome del gruppo
#     - get_limit(): Restituisce il limite di studenti nel gruppo
#     - get_students(): Resituisce la lista di studenti nel gruppo
#     - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
#     - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
#     - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.

# ### Classe Course:
# La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# - Metodi:
#     - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
#     - get_groups(): Restituisce la lista dei gruppi nel corso.
#     - add_group(group): Aggiunge un gruppo al corso.

class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id: str=id
        self.floor: int=floor
        self.seats: int=seats
    def get_id(self) -> str:
        return self.id
    def get_floor(self) -> int:
        return self.floor
    def get_seats(self) -> int:
        return self.seats
    def get_area(self) -> int: 
        return self.seats*2

class Building:
    def __init__(self, name: str, address: str, floors: tuple[int]) -> None:
        self.name: str=name
        self.address: str=address
        self.floors: tuple[int]=floors
        self.rooms: list[Room]=[]
    def get_floors(self) -> tuple[int]:
        return self.floors
    def get_rooms(self) -> list[Room]:
        return self.rooms
    def add_room(self, room: Room) -> None:
        self.rooms.append(room) if room.floor in range(self.floors[0], self.floors[1]+1) and room not in self.rooms else None
    def area(self) -> float:
        return sum([room.get_area() for room in self.rooms])

class Person:
    def __init__(self, cf: str, name: str, surname: str, age: str) -> None:
        self.cf: str=cf
        self.name: str=name
        self.surname: str=surname
        self.age: int=age

class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: str) -> None:
        super().__init__(cf, name, surname, age)
        self.group=None
    def set_group(self, group: 'Group') -> None:
        group.add_student(self)

class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: str) -> None:
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name: str, limit: int) -> None:
        self.name: str=name
        self.limit: int=limit
        self.students: list[Student]=[]
        self.lecturers: list[Lecturer]=[]
    def get_name(self) -> str:
        return self.name
    def get_limit(self) -> int:
        return self.limit
    def get_students(self) -> list[Student]:
        return self.students
    def get_limit_lecturers(self) -> int:
        return len(self.students)//10+1
    def add_student(self, student: Student) -> None:
        if student not in self.students and len(self.students)<self.limit: student.group=self; self.students.append(student)
    def add_lecturer(self, lecturer: Lecturer) -> None:
        if lecturer not in self.lecturers and len(self.lecturers)<self.get_limit_lecturers(): self.lecturers.append(lecturer)

class Course: 
    def __init__(self, name: str) -> None:
        self.groups: list[Group]=[]
    def register(self, student: Student) -> None:
        for group in self.groups:
            if len(group.students)<group.limit:
                group.add_student(student)
                break
    def get_groups(self) -> list[Group]:
        return self.groups
    def add_group(self, group: Group) -> None:
        if group not in self.groups: self.groups.append(group)


# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")