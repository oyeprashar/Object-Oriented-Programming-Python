from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def personMethod(self):
        pass

class Student(Person):

    def personMethod(self):
        print("I'm a student")


class Teacher(Person):

    def personMethod(self):
        print("I'm a teacher")


class PersonFactory:

    @staticmethod
    def getPerson(type):
        if type == "Student":
            return Student()

        elif type == "Teacher":
            return Teacher

        return None
