class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def register(self):
        print("original method")


class CollegeStudent(Student):

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old"

    # we can overwrite the function of inherited class
    def register(self):
        print("method overwritten")


cs = CollegeStudent("Shubham", 21)
print(cs)
cs.register()
