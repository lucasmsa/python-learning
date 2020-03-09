# a module that allows using iterators in a fast 
# and memory efficient way

import itertools
import time

# without any parameter count will start in zero and increment its 
# value by one at each iteration
# the step parameter will change 
# the leap from one iteration to the other

""" #counter = itertools.count(start=1, step=3)

#for number in counter:
#    print(number)
#    time.sleep(0.5) """

# the cycle method will loop through the iterables forever
""" # counter = itertools.cycle(['banana', 'maca', 'uva'])

# for word in counter:
#     print(word)
#     time.sleep(0.5) """

# repeat method will repeat the value passed to it
# it's also possible to set the number of times 
# it will repeat the value through the parameter times 

""" # counter = itertools.repeat(10, times=5)
 """
# one example using the map function
""" squares = map(pow, range(10), itertools.repeat(2))
print(list(squares)) """

# there`s also the starmap method
# that works like a map but instead it will 
# take its arguments as a list of tuples

""" squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)])
print(list(squares))
 """

# there are also functions that return all the possible
# combinations (order does not matter) // permutations (order matters) 
# of some data



# the second parameter is used to set how many 
# values will be tested, 
# ex.: (2) -> ab, cd ...
#      (3) -> abc, bcd ...

""" letters = ['a', 'b', 'c', 'd', 'e'] 
result = itertools.combinations(letters, 2)

for item in result:
    print(item) """

# permutations are really similar, but the order
# does matter. ('a', 'b') != ('b', 'a')

"""
result = itertools.permutations(letters, 2)

for item in result:
    print(item) """

# the product method will check for every permutation
# possible repeating values ex.: 0000 will be valid in the case
# below. It can be used as a password cracker
""" 
nums = [0, 1, 2]
result = itertools.product(nums, repeat=4)

for index, item in enumerate(result):
    print(index, item)
 """

# it's also possible to have combinations with repetition
""" 
result = itertools.combinations_with_replacement(nums, 4)
 """

# there's also the chain method that allows looping through 
# a sequence of iterable data

""" 
names = ['gott', 'chacrinha']

result = itertools.chain(letters, nums, names)

for item in result:
    print(item) """

# islice gets the slice of an iterator
""" result = itertools.islice(range(10), 5)

for item in result:
    print(item) """

# compress method
# will pass two iterables and it will only return
# values that have a corresponding true value
# similar to filter, but in this function
# the values are passed in as an iterable, not as a function
"""
selectors = [True, False, True, True, False]

result = itertools.compress(data=letters, selectors=selectors)

for item in result:
    print(item)
 """

# filterfalse, like the built-in filter function
# but it will return the False values
""" result = itertools.filterfalse(someFunction, someListOfValues) """

# filters the values until one value returns false
# then it stops applying the filter, afterwards it will return 
# all of the remaining values
""" result = itertools.dropwhile(someFunction, someListOfValues) """

# returns the values until one value returns false
# then it stops applying the filter, afterwards it will not return 
# any other remaining value
""" result = itertools.takewhile(someFunction, someListOfValues) """

# accumulate returns a sum of the values at each new iteration
""" result = itertools.accumulate(nums) """

# groupby groups values based on a certain key and returns a string of tuples
# with the keys that the values were grouped by. And the second value contains 
# the iterators with all of the values that were grouped by that key

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def getState(person):
    return person['state']

# getState will act as the that the iterable will be grouped by
result = itertools.groupby(people, getState)

# tee method copies an iterable, when the copy is made
# it is recommended to not use the iterable that was copied
# anymore 
copyResult = itertools.tee(result)

for key, group in result:
    
    print(key)
    # group represents the people that are in the 
    # determined state, that acts as the key
    for item in group:
        print(item)
    
    print()


