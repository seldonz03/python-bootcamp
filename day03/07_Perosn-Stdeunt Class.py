class Person:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def introduction(self):
        return f"I'm{self.first_name}{self.last_name}!"
    def sleep(self):
        print("I will sleep eight hours")

class Student(Person):
    def __init__(self, first_name, last_name,level):
        super().__init__(first_name,last_name)
        self.l=level

    def introduction(self):
        return super().introduction() + f"I'm a {self.l} student."




student1 = Student("Juan", 'Odonzo', "3rd Level")
print(student1.introduction())
