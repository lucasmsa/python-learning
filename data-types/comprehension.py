nList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#myList = []
#for n in nList:
#    myList.append(n)

myList = [n for n in nList]
print(myList)

# map runs everything on the list through a certain function
# lambda is an anonymous function

myLambdaList = map(lambda n: n*n, nList)
print(list(myLambdaList))

# n for each n in nums if n is even
#myList = []
#for n in nList:
#   if n%2 == 0:
#       myList.append(n)

myEvenList = [n for n in nList if n%2 == 0]
print(myEvenList)

# letter, num for each letter in 'abcd' and each number in '0123'
#myList = []
#for letter in 'abcd':
#   for n in range(4):
#       myList.append(letter, n)

myLetterNumbersList = [(letter, num) for letter in 'abcd' for num in range(4)]
print(myLetterNumbersList)

# Zip function matches 2 different data into a tuple

names = ['bruce', 'clark', 'logan', 'peter', 'arthur']
heroes = ['batman', 'superman', 'wolverine', 'spider-man', 'aquaman']

print(list(zip(names, heroes)))

# Dict { 'name': 'hero'} for each name, hero in zip(names, heroes)
# myDict = {}
# for name, hero in zip(names, heroes):
#   myDict[name] = hero
    
myDict = { k: v for k, v in zip(names, heroes)}
print(myDict)

# set comprehension
mySet = {n for n in names}
print(mySet)

# Generator comprehension
myGen = (n*n for n in nList)

for i in myGen:
    print(i)