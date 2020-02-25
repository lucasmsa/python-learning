# LISTS

listEx = []
listEx = ['Pig', 'Cow', 'Fish']
listEx2 = ['Rat', 'Turtle']
nums = [83, 421, 33, 72, 2]

# Gets the last element, no need for listEx[len(listEx)]
listEx.append('Salmon')
listEx.insert(2, 'Zebra')

# Extend method will get each individual item from another list and append them to the list in question
listEx.extend(listEx2)

listEx.remove('Fish')


print(listEx[-2:]) 

print(listEx) 
listEx.reverse()
print(listEx)

# Sort in descending order
nums.sort(reverse=True) 

# One other way to sort list that won't alter the original list is by using sorted()
sortedNums = sorted(nums)

#There are also min(list), max(list) and sum(list) which are self explanatory
max(nums)

#To find the index of a certain item
print(listEx.index('Cow'))

print(nums, sortedNums)

# One way to loop through a list, start is a second parameter and it will not necessarily will be passed
for index, element in enumerate(listEx, start=1):
    print(index, element)

    if index == len(listEx) - 1:
        print('Cabou')

# The join function
# Separate by ', ' each item in the list

listExStr = ', '.join(listEx)

print(listExStr)


# TUPLES
# Tuples cannot be modified

tupleEx1 = ('Sopa', 'de', 'macaco')
tupleEx2 = tupleEx1

# The next line will return an error
# tupleEx1[0] = 'geleia' 


# SETS 
# Unordered data type, it will change the order each time you rerun the code
# Mostly used for checking if an item is in the set, they are optimized for this
setEx = {'bolsa','cadeira','teclado','mouse'}
setEx2 = {'teclado', 'mouse', 'mousepad', 'monitor'}

print(setEx)

# Sets are also pretty efficient checking equal items between different sets
print(setEx.intersection(setEx2))

# Or checking different items
print(setEx.difference(setEx2))

# Also, they can be merged
print(setEx.union(setEx2))