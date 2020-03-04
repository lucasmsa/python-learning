import sqlite3
from test_sqlite import Person

# connects to the db or creates it
connection = sqlite3.connect('person.db')

# creates a new database that stays in RAM, and is created at each new execution
#connection = sqlite3.connect(':memory:')

# cursor is used to execute sql commands
cursor = connection.cursor()

# SQL commands that use multiple lines are wrapped in triple quotes, also called docstrings
# SQLite data types, NULL, INTEGER, BLOB, TEXT, REAL

#cursor.execute("""CREATE TABLE people (
#                fName text,
#                lName text,
#                age integer
#                )""")

def insert_emp(person):
    with connection:
        cursor.execute("INSERT INTO people VALUES (:fName, :lName, :age)", {'fName': person.name, 'lName': person.lastName, 'age': person.age})

def get_person_by_name(name):
    cursor.execute("SELECT * FROM people WHERE fName=:fName", {'fName' : name})
    return cursor.fetchall()

def delete_person(person):
    with connection:
        cursor.execute("Delete FROM people WHERE lName=:lname AND fName=:fName", { 'fName': person.name, 'lName': person.lastName })

# creating random people to insert into db
person_1 = Person('Shao', 'khan', 100)
person_2 = Person('Quan', 'Chi', 80)


# put values as a tuple into the table
#cursor.execute("INSERT INTO people VALUES (?, ?, ?)", (person_1.name, person_1.lastName, person_1.age))
#connection.commit()


# put values as a dictionary into the table
# despite being longer, it's much more readable than passing it as a tuple
#cursor.execute("INSERT INTO people VALUES (:fName, :lName, :age)", {'fName': person_2.name, 'lName': person_2.lastName, 'age': person_2.age})
#connection.commit()

#cursor.execute("Delete FROM people WHERE lName='khan'")

cursor.execute("SELECT * FROM people WHERE fName=:lName", {'lName' : 'Chi'})
# return as a list, or return an empty list
print(cursor.fetchall())


# commit the step to the database, note that the connection is commited
connection.commit()


connection.close()