import logging

# gets the right log settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# format that will be printed in the log file
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# log file name and sets the format defined by formatter
file_handler = logging.FileHandler('person.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Person:

    def __init__(self, name, lastName, age):
        
        self.name = name
        self.lastName = lastName
        self.age = age

        logger.info(f'Created peson. Name: {self.name} {self.lastName}, age: {self.age}')

    @property
    def email(self):
        return f'{self.name}-{self.lastName}@email.com'

    def __repr__(self):

        return f'Person({self.name}, {self.lastName}, {self.age})'


pato = Person('Alexandre', 'Pato', 25)
