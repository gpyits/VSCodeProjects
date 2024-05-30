# Exercise 1 - Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.


# Exercise 2 - Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.


# Exercise 3 - Library Management System 
# - Create a Book class containing the following attributes: title, author, isbn
#       The book class must contains the following methods:
#               - __str__ method to return a string representation of the book.
#               - @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
#               - It means that you must use the class reference cls to create a new object of the Book class using a string.
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


# Exercise 4 - University Management System
# Create a system to manage a university with departments, courses, professors, and students. 
# - Create an abstract class Person:
#       Attributes:
#          - name (string)
#          - age (int)
#       Methods:
#          - __init__ method to initialize the attributes.
#          - Abstract method get_role to be implemented by subclasses.
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