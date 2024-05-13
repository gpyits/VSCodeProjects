'''
Module used for studying the classes in python.

Returns:
    Person: Class describing a person
'''

# Python classes:

# Create a Class that represents a Person
# first_name, last_name, ssn
# birth_date, birth_place, gender

# Define all getters and setters
# Define a method that calculates ssn (and update for every possible change)

from typing import Literal

class Person:
    '''
    A class offering a general description of a person and
    a method to generate theirs social security number.
    '''

    def __init__(self, first_name: str, last_name: str, **kwargs: str) -> None:

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.birth_date: str = ""
        if kwargs.get('birth_date'):
            self.birth_date: str = kwargs["birth_date"]
        self.birth_place: str = ""
        if kwargs.get('birth_place'):
            self.birth_place: str = kwargs["birth_place"]
        self.gender: str = ""
        if kwargs.get('gender'):
            self.gender: Literal["Maschio","Femmina","M","F"] = kwargs["gender"]
        self._ssn: str = ""
        if kwargs.get('birth_date') and kwargs.get('birth_place') and kwargs.get('gender'):
            self._ssn: str = self.update_ssn()

    def get_first_name(self) -> str:
        '''
        This method is used to get the variable first_name.

        Returns:
            str: self.first_name
        '''
        return self.first_name

    def get_last_name(self) -> str:
        '''
        This method is used to get the variable last_name.

        Returns:
            str: self.last_name
        '''
        return self.last_name

    def get_birth_date(self) -> str:
        '''
        This method is used to get the variable birth_date.
        If the variable is empty it returns None.

        Returns:
            str: self.birth_date
        '''
        return self.birth_date if self.birth_date else None

    def get_birth_place(self) -> str:
        '''
        This method is used to get the variable birth_place.
        If the variable is empty it returns None.

        Returns:
            str: self.birth_place
        '''
        return self.birth_place if self.birth_place else None

    def get_gender(self) -> str:
        '''
        This method is used to get the variable gender.
        If the variable is empty it returns None.

        Returns:
            str: self.gender
        '''
        return self.gender if self.gender else None

    def get_ssn(self) -> str:
        '''
        This method is used to get the variable _ssn.
        If the varial is empty it returns None.

        Returns:
            str: self._ssn
        '''
        return self._ssn

    def set_first_name(self, first_name: str) -> None:
        '''
        This method is used to change the variable first_name.

        Args:
            first_name (str): will replace self.first_name
        '''
        self.first_name = first_name
        self._ssn: str = self.update_ssn()

    def set_last_name(self, last_name: str) -> None:
        '''
        This method is used to change the variable last_name.

        Args:
            last_name (str): will replace self.last_name
        '''
        self.last_name = last_name
        self._ssn: str = self.update_ssn()

    def set_birth_date(self, birth_date: str) -> None:
        '''
        This method is used to change the variable birth_date.

        Args:
            birth_date (str): will replace self.birth_date
        '''
        self.birth_date = birth_date
        self._ssn: str = self.update_ssn()

    def set_birth_place(self, birth_place: str) -> None:
        '''
        This method is used to change the variable birth_place.

        Args:
            birth_place (str): will replace self.birth_place
        '''
        self.birth_place = birth_place
        self._ssn: str = self.update_ssn()

    def set_gender(self, gender: str) -> None:
        '''
        This method is used to change the variable gender.

        Args:
            gender (str): will replace self.gender
        '''
        self.gender = gender
        self._ssn: str = self.update_ssn()

    def update_ssn(self) -> str:
        '''
        This is used to calculate the ssn based on Codice Fiscale.
        It requires first_name, last_name, birth_date, birth_place and gender.
        '''
        import re

    def __str__(self) -> str:
        '''
        This method is used to return a full string with information about the Person.

        Returns:
            str: Variable string with information stored in the Person.
        '''

person1: Person = Person("Luca", "Committeri",
                         birth_date= "21/04/2000", birth_place= "Roma", gender= "M")
person2: Person = Person("Marco", "Ciccia")
person3: Person = Person("Giacomo", "Palermitano",
                         birth_place= "Venezia") 
person4: Person = Person("Maria","Granula",
                         birth_date="09/07/1969", birth_place= "Palermo", gender= "F")
print(str(person1))
print(str(person2))
print(str(person3))
print(str(person4))
