from classAndInstances import Employee

# Creates a new class that inherits from Employee
class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self, first, last, pay, progLang):
        # Init the values inherited
        super().__init__(first, last, pay)
        self.progLang = progLang

dev1 = Developer('Car', 'Code', 100000, 'Python')
dev2 = Developer('Jimmy', 'Sharp', 300000, 'Javascript')

# Helps visualizing each and every aspect of the class
# print(help(Developer))

class Manager(Employee):

    def __init__(self, first, last, pay, supervised=None):
        super().__init__(first, last, pay)
        if supervised is None:
            self.supervised = []
        else:
            self.supervised = supervised

    def addEmp(self, emp):
        if emp not in self.supervised:
            self.supervised.append(emp)

    def removeEmp(self, emp):
        if emp in self.supervised:
            self.supervised.remove(emp)

    def printEmp(self):
        for emp in self.supervised:
            print('-> ' + emp.fullName())


manager1 = Manager('Cal', 'Douglas', 1000000, [dev1])

print(manager1.email)
manager1.printEmp()

manager1.addEmp(dev2)
manager1.printEmp()

