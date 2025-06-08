class Student:
    def __init__(self,name,level):
        self.n = name
        self.l = level

    def introduction(self):
        return f"I'm {self.n}! Im'a {self.l} student."


student1 = Student("Juan", '3rd year College')
print(student1.introduction())

student2 = Student("Maria", 'Grade Three')
print(student2.introduction())