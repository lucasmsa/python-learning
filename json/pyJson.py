import json

# Normal json file notation
peopleString = '''
{
    "people": [
        {
            "name": "Johan",
            "age": 23,
            "emails": ["jk@email.com","superjk@semail.com"] 
        },
        {
            "name": "latika",
            "age": 17,
            "emails": ["latoka@email.com","lat@semail.com"] 
        }
    ]
}
'''

# loads for loading strings
dataJson = json.loads(peopleString)
# json objects are converted to python dictionaries
print(type(dataJson))
print(dataJson)

# Accessing the dictionaries inside the 'people' key
for person in dataJson['people']:
    # Delete person key
    # del person['emails']
    print(person['name'])

# indent method for improved readability
# sort_keys to sort keys alphabetically
newStr = json.dumps(dataJson, indent=2, sort_keys=True)
print(newStr)

# US states
with open('states.json') as f:
    # load for loading files
    dataJsonStates = json.load(f)

for state in dataJsonStates['states']:
    del state['area_codes']
    print(state['name'], state['abbreviation'])
    
with open('statesNoAreaCodes.json', 'w') as f:
    json.dump(dataJsonStates, f, indent=2)
