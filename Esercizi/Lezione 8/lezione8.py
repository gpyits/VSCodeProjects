from abc import *
# Exercise 1 - Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
class Shape(ABC):
    @abstractmethod
    def perimeter(self) -> int:
        pass
    @abstractmethod
    def area(self) -> int:
        pass

class Circle(Shape):
    def __init__(self, radius: int) -> None:
        super().__init__()
        self.radius: int=radius
    def perimeter(self) -> int:
        return 2*3.14*self.radius
    def area(self) -> int:
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self, side_1: int, side_2: int) -> None:
        super().__init__()
        self.side_1: int=side_1
        self.side_2: int=side_2
    def perimeter(self) -> int:
        return (self.side_1+self.side_2)*2
    def area(self) -> int:
        return self.side_1*self.side_2
    
# Exercise 2 - Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.
class MathOperations:
    @staticmethod 
    def add(num1: int, num2: int) -> int:
        return num1+num2
    @staticmethod
    def multiply(num1: int, num2: int) -> int:
        return num1*num2

MathOperations.add(1, 3)
# Exercise 3 - Library Management System 
# - Create a Book class containing the following attributes: title, author, isbn
#       The book class must contains the following methods:
#               - __str__ method to return a string representation of the book.
#               - @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
#                 It means that you must use the class reference cls to create a new object of the Book class using a string.
#
# Example: 
# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with  title = La Divina Commedia, author = D. Alighieri, isbn = 999000666
#
# - Create a Member class with the following attributes: name, member_id, borrowed_books
#       The member class must contain the following methods:
#               - borrow_book(book) to add a book to the borrowed_books list.
#               - return_book(book) to remove a book from the borrowed_books list.
#               - __str__ method to return a string representation of the member.
#               - @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".
#
# - Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
#       The library class must contain the following methods:
#               - add_book(book) to add a book to the library and increment total_books.
#               - remove_book(book) to remove a book from the library and decrement total_books.
#               - register_member(member) to add a member to the library.
#               - lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.
#               - __str__ method to return a string representation of the library with the list of books and members.
#               - @classmethod library_statistics(cls) to print the total number of books.
#
# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library. Lend books to members and display the state of the library before and after lending.
class Book:
    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title: str=title
        self.author: str=author
        self.isbn: int=isbn
        self.is_available=True
    def __str__(self) -> str:
        return f'{self.title}, {self.author}, {self.isbn}'
    @classmethod
    def from_string(cls, book_string: str) -> object:
        title, author, isbn=book_string.split(', ')
        return Book(title, author, isbn)

class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name: str=name
        self.member_id: str=member_id
        self.borrowed_books: list[Book]=[]
    def borrow_book(self, book: Book) -> None:
        if book not in self.borrowed_books: self.borrowed_books.append(book); book.is_available=False
    def return_book(self, book: Book) -> None:
        if book not in self.borrowed_books: self.borrowed_books.remove(book); book.is_available=True
    def __str__(self) -> str:
        return f'{self.name}, {self.member_id}'
    @classmethod
    def from_string(cls, member_str: str) -> object:
        name, member_id=member_str.split(', ')
        return Member(name, member_id)

class Library:
    total_books: int=0
    def __init__(self) -> None:
        self.books: list[Book]=[]
        self.members: list[Member]=[]
    def add_book(self, book:Book) -> None:
        if book not in self.books: self.books.append(book); total_books+=1
    def remove_book(self, book: Book) -> None:
        if book.id in self.books: self.books.remove(book); total_books-=1
    def register_member(self, member: Member) -> None:
        if member.id not in self.members: self.members.append(member)
    def lend_book(self, book: Book, member: Member) -> None:
        if member in self.members:
            if book in self.books and book.is_available: member.borrow_book(book)
            else: raise ValueError('Book is not available')
        else: raise ValueError('Member is not registered')
    def __str__(self) -> str:
        return f'Library with books={self.books} and members={self.members}'
    @classmethod
    def library_statistics(cls) -> None:
        print(cls.total_books)

# Exercise 4 - University Management System
# Create a system to manage a university with departments, courses, professors, and students. 
# - Create an abstract class Person:
#       Attributes:
#          - name (string)
#          - age (int)
#       Methods:
#          - __init__ method to initialize the attributes.
#          - @abstractmethod get_role to be implemented by subclasses.
#          - __str__ method to return a string representation of the person.
#
# - Create subclasses Student and Professor that inherit from Person and implement the abstract methods:
#       Student:
#          - Additional attributes: student_id (string), courses (list of Course instances)
#          - Method enroll(course) to enroll the student in a course.
#       Professor:
#          - Additional attributes: professor_id (string), department (string), courses (list of Course instances)
#          - Method assign_to_course(course) to assign the professor to a course.
#
# - Create a class Course:
#       Attributes:
#          - course_name (string)
#          - course_code (string)
#          - students (list of Student instances)
#          - professor (Professor instance)
#       Methods:
#          - __init__ method to initialize the attributes.
#          - add_student(student) to add a student to the course.
#          - set_professor(professor) to set the professor for the course.
#          - __str__ method to return a string representation of the course.
#
# - Create a class Department:
#       Attributes:
#          - department_name (string)
#          - courses (list of Course instances)
#          - professors (list of Professor instances)
#       Methods:
#          - __init__ method to initialize the attributes.
#          - add_course(course) to add a course to the department.
#          - add_professor(professor) to add a professor to the department.
#          - __str__ method to return a string representation of the department.
#
# - Create a class University:
#       Attributes:
#          - name (string)
#          - departments (list of Department instances)
#          - students (list of Student instances)
#       Methods:
#          - __init__ method to initialize the attributes.
#          - add_department(department) to add a department to the university.
#          - add_student(student) to add a student to the university.
#          - __str__ method to return a string representation of the university.
#
# Create a script:
#   1. Create instances of departments, courses, professors, and students.
#   2. Add them to the university.
#   3. Enroll students in courses and assign professors to courses.
#   4. Display the state of the university.
class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        super().__init__()
        self.name: str=name
        self.age: int=age
    @abstractmethod
    def get_role() -> None:
        pass
    def __str__(self) -> None:
        return f'{self.name}, {self.age}'
    
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id: str=student_id
        self.courses: list[Course]=[]
    def enroll(self, course: object):
        self.courses.append(str(course))
    def get_role(self):
        return 'Role: student'

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str) -> None:
        super().__init__(name, age)
        self.professor_id: str=professor_id
        self.courses: list[Course]=[]
    def assign_to_course(self, course: object):
        self.courses.append(str(course))
    def get_role(self):
        return 'Role: professor'

class Course:
    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name: str=course_name
        self.course_code: str=course_code
        self.students: list[Student]=[]
        self.professor: Professor=None
    def add_student(self, student: Student):
        if student not in self.students: self.students.append(str(student))
    def set_professor(self, professor: Professor):
        if self.professor: self.professor.courses.remove(str(self))
        self.professor=professor, professor.courses.append(str(self))
    def __str__(self) -> str:
        return f'Course {self.course_code}:{self.course_name} with students={self.students} and professor={self.professor}'

class Department:
    def __init__(self, department_name: str) -> None:
        self.department_name: str=department_name
        self.courses: list[Course]=[]
        self.professors: list[Professor]=[]
    def add_course(self, course: Course):
        if course not in self.courses: self.courses.append(str(course))
    def add_professor(self, professor: Professor):
        if professor not in self.professors: self.professors.append(str(professor))
    def __str__(self) -> str:
        return f'Department {self.department_name} with courses={self.courses} and professors={self.professors}'

class University:
    def __init__(self, name: str) -> None:
        self.name: str=name
        self.departments: list[Department]=[]
        self.students: list[Student]=[]
    def add_department(self, department: Department):
        if department not in self.departments: self.departments.append(str(department))
    def add_student(self, student: Student):
        if student not in self.students: self.students.append(str(student))
    def __str__(self) -> str:
        return f'University {self.name} with departments={self.departments} and students={self.students}'

physics: Department = Department("physics")
engineering: Department = Department("engineering")
science: Department = Department("science and technology")

quantum: Course = Course("quantum physics", "p001")
relativity: Course = Course("relativity", "p002")
astro: Course = Course("astrophysics", "p003")
aerospace: Course = Course("aerospace engineering", "e001")
computer: Course = Course("computer engineering", "e002")
bio: Course = Course("bioengineering", "e003")
chem: Course = Course("chemistry", "s001")
math: Course = Course("mathematics", "s002")
geology: Course = Course("geology", "s003")

lupin: Professor = Professor("Remus Lupin", 38, "hgw001")
hagrid: Professor = Professor("Rubeus Hagrid", 54, "hgw002")
snape: Professor = Professor("Severus Snape", 38, "hgw003")
dyer: Professor = Professor("William Dyer", 33, "hpl0v3")
kirke: Professor = Professor("Digory Kirke", 61, "csl3w1s")
otto: Professor = Professor("Otto Liedenbrock", 42, "v3rn3")
moriarty: Professor = Professor("James Moriarty", 70, "c0n4nd0yl3")
langdon: Professor = Professor("Robert Langdon", 47, "t0mh4nk5")
keating: Professor = Professor("John Keating", 32, "d34dp03t5")

alfred: Student = Student("Alfred Hutheesing", 20, "std001")
freedon: Student = Student("Freedon Annunziato", 21, "std002")
alan: Student = Student("Alan Tucker", 19, "std003")
jenny: Student = Student("Jenny Coleman", 20, "std004")
yvonne: Student = Student("Yvonne William", 20, "std005")
eric: Student = Student("Eric Da Silva", 22, "std006")

hailsmith: University = University("hailsmith")

alfred.enroll(quantum)
alfred.enroll(computer)
alfred.enroll(math)
freedon.enroll(bio)
freedon.enroll(chem)
freedon.enroll(math)
alan.enroll(quantum)
alan.enroll(relativity)
jenny.enroll(bio)
jenny.enroll(geology)
jenny.enroll(astro)
yvonne.enroll(aerospace)
yvonne.enroll(astro)
yvonne.enroll(relativity)
eric.enroll(computer)
eric.enroll(quantum)
eric.enroll(math)

snape.assign_to_course(math)
lupin.assign_to_course(astro)
hagrid.assign_to_course(bio)
dyer.assign_to_course(relativity)
kirke.assign_to_course(chem)
moriarty.assign_to_course(quantum)
otto.assign_to_course(geology)
langdon.assign_to_course(computer)
keating.assign_to_course(aerospace)

physics.add_course(quantum)
physics.add_course(relativity)
physics.add_course(astro)
engineering.add_course(bio)
engineering.add_course(aerospace)
engineering.add_course(computer)
science.add_course(chem)
science.add_course(math)
science.add_course(geology)

physics.add_professor(dyer)
physics.add_professor(moriarty)
physics.add_professor(lupin)
engineering.add_professor(hagrid)
engineering.add_professor(keating)
engineering.add_professor(langdon)
science.add_professor(snape)
science.add_professor(kirke)
science.add_professor(otto)

hailsmith.add_department(physics)
hailsmith.add_department(engineering)
hailsmith.add_department(science)
hailsmith.add_student(alfred)
hailsmith.add_student(yvonne)
hailsmith.add_student(eric)
hailsmith.add_student(freedon)
hailsmith.add_student(alan)
hailsmith.add_student(jenny)

print(str(hailsmith))