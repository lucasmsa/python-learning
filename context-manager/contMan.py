from contextlib import contextmanager
import os

# Used to handle custom resources
# A with open() is qualified as a context manager
# as it automates some of the tasks for the user 
# like having to close a file

# Tutorial to write out a context manager
# Generally it will be made by using a class 
# or by using a function decorator

# __enter__ and __exit__ methods are made to setup and destroy the 
# context manager
class OpenFile():
    
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file, self.mode)
        return self.file

    def __exit__(self, excType, excVal, traceback):
        self.file.close()


# Sets each method
# f is the return object from the __enter__ method
# the __exit__ method is ran when the identation of the
# with changes
with OpenFile('cmClass.txt', 'w') as f:
    f.write("sup")


# with decorators
@contextmanager
def open_file(file, mode):
    try:
        # creates and opens file
        # equivalent to __enter__ class method
        f = open(file, mode)
        # where the code inside the with statement will run 
        yield f
    finally:
        # similar to the __exit__ class method
        f.close()

with open_file('cmDecorator.txt','w') as f:
    f.write('suer')

# Tells if the file is closed or not
print(f.closed)
  

# A more practical example, envolving changing directories
# and list files in directory

@contextmanager
def changeDir(dest):
    try:
        cwd = os.getcwd()
        os.chdir(dest)
        yield
    finally:
        os.chdir(cwd)

with changeDir('dir'):
    print(os.listdir())