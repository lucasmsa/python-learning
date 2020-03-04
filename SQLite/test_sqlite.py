# Good for database functionality without having to use 
# a bigger database like postGreSQL. Used in small to medium-sized projects


# class used for filling in the database
class Person:

    def __init__(self, name, lastName, age):
        
        self.name = name
        self.lastName = lastName
        self.age = age

    @property
    def email(self):
        return f'{self.name}-{self.lastName}@email.com'

    def __repr__(self):

        return f'Person({self.name}, {self.lastName}, {self.age})'

