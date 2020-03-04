# To determine that a string is going to be a f-string simply put f' before it

name = 'mucas'
lastName = 'loreira'

# The placeholders are added directly to the string, no need for .format()
phrase = f'name is {name.upper()} {lastName.lower()}'
print(phrase)

# Using f-string with dictionaries
personDict = {'name': 'Mucas', 'age': 42}

# Using different quotes when accessing dict keys
phrase = f'name is {personDict["name"]}, age {personDict["age"]}'
print(phrase)

calc = f'2 + 2 = {2+2}'
print(calc)

for n in range(10):
    phrase = f'value: {n:02}'
    print(phrase)