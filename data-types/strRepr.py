a = [1, 2, 3, 4]
b = 'sampleStr'

# In a list, str and repr representation are the same
print(str(a))
print(repr(a))

# In a string, the str version is printed without quotes
# repr with quotes, the difference is not so clear 
print(str(b))
print(repr(b))

# Goal of str is to be readable
# Goal of repr is to be unambiguous, repr() representations tend to 
# look more like a python command, and are good for debugging