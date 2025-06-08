class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.r = role
        self.tasks=[]
        print(f"Employee {self.name} assigned ID {self.id} position{role})")
    def add_work(self, task):
        return self.tasks.append(task)


employee1 = Employee("Richard","1234","IT")
employee2 = Employee("Jelly","9867","Manager")

print("Employee1 Name:", employee1.r)
print("Employee2 Name:",employee2.r)

employee1.add_work("create charts")
print(employee1.tasks)
