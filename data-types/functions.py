# Important heads up
def testArgs(*args, **kwargs):
    print(args)
    print(kwargs)

# The firs argument, args, are passed as a tuple and the second one
# as a dictionary
testArgs('math', 1, 'garrafa pet', name='lucas', age=21)

# To unpack the values and pass them to through your function correctly

firstArg = ['math', 1, 'garrafa pet']
secondArg = {'name': 'lucas', 'age': 21}

# Pass with '*'
testArgs(*firstArg, **secondArg)

