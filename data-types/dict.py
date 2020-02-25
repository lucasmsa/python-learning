# Work with key-value pairs

dictTest = {'name' : 'Luka Magnotta', 'age' : 32}

# Preferably use .get method, because it will return None if the item isn't in the dictionary
# Instead of dictTest['name'], you can set the default value for keys that don't exist by setting an extra parameter
print(dictTest.get('name'))
print(dictTest.get('pepper', 'NOOO'))

# Update method to add new key-value pairs
dictTest.update({'garrafa': 'pet'})

print(dictTest)

# Delete items through 
# del dictTest['name']
# or
# age = dictTest.pop('age')

# Access all items 
print(dictTest.items())


# Doing a normal for in the dict will only get the keys
for k, v in dictTest.items():
    print(k, v)

