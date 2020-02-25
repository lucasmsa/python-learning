class Employee:
        
    # if I just wanted to create it and do nothing
    # pass
    
    # class variable
    numOfEmps = 0
    raiseAmount = 1.04
        
    # constructor
    def __init__(self, first, last, pay):
                
        self.first = first
        self.last = last
        self.pay = pay

        Employee.numOfEmps += 1

    # Define attribute as a method
    # call it as emp1.email
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        self.first = None
        self.last = None

     # Regular method
    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

    # Class method
    # Receives the class as the first argument
    # instead of the instance
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount
    
    # Dinamically create new employees with strings
    @classmethod
    def fromString(cls, empStr):
        first, last, pay = empStr.split('-')
        return cls(first, last, pay)

    # static method, the first parameter is null
    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 5:
            return False
        return True

    # Change how our objects are printed and displayed
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullName, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName)



# Instance variable
emp1 = Employee('Eric', 'Butler', 100000)
emp2 = Employee('James', 'Deen', 80000)

# Get the __str__ dunder method
print(emp1)
print(emp1.fullName)

# Get the __add__ dunder method
print(emp1 + emp2)


# Get the __len__ dunder method
print(len(emp1))


# It will change all class instances
Employee.setRaiseAmount(1.06)
# Same thihng as
# Employee.raiseAmount = 1.06

print(emp1.pay)
emp1.applyRaise()
print(emp1.pay)



# Changes the class variable only in the instance
# Due to the fact that it is self.raiseAmount in the class
# emp1.raiseAmount = 1.05

# Changes the class variable
# emp1.raiseAmount = 1.05

# Access class instances attributes as a dict
print(emp1.__dict__)

print(Employee.numOfEmps)


emp3Str = 'John-Doe-120000'
emp3 = Employee.fromString(emp3Str)

import datetime
myDate = datetime.date(2020, 2, 25)

print(emp3.first)
print(emp3.isWorkDay(myDate))


