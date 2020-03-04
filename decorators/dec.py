# Decorators are functions that take another function as an argument, adds some kind of funcionality
# and returns another function

# Easy to add functionality, by adding that functionality inside of the wrapper
 
def decoratorFunction(originalFunction):
    def wrapperFunction(*args, **kwargs):
        print(f'wrapper exectuted: {originalFunction.__name__}')
        return originalFunction(*args, **kwargs)

    # return wrapperFunction that is waiting to be executed 
    # and when it is, it executes the originalFunction
    return wrapperFunction


# It is also possible to use decorators with classes
def decoratorClass(object):

    def __init__(self, originalFunction):
        self.originalFunction = originalFunction

    def __call__(self, *args, **kwargs):
        print(f'wrapper exectuted: {self.originalFunction.__name__}')
        return self.originalFunction(*args, **kwargs)


# (*)
@decoratorFunction
def display():
    print('Display')

# without - (*) -> decDisplay = decoratorFunction(display)
# same as with (*)
display()

# With arguments, call in the decorator as funct(*args, **kwargs)
@decoratorFunction
def displayInfo(name, age):
    print(f'Display: ({name}, {age})')

displayInfo('John', 23)



