s1 = set([1, 2, 3, 4, 5])
# or
# s1 = {1, 2, 3, 4, 5}

s2 = {9, 10}

s3 = {4, 5}

s4 = {5, 6, 7}

s5 = {6, 7, 8}
# sets remove duplicate values
# add values in sets
s1.add(6)
# add multiple values
s1.update([6, 7, 8], s2)
s1.remove(6)

print(s1)

# gets intersenction
print(s1.intersection(s3))
print(s1.intersection(s3, s4))

# gets values that are not in the set that the method runs
print(s3.difference(s4)) 


# gets all of the differences between sets 
print(s3.symmetric_difference(s4))


# to remove duplicates in a list you can simply
# listWithoutDuplicates = list(set(listWithDuplicates))
# other operations like difference and intersection can also be made


# convert list in sets to check for 
# 'item' in list -> O(n) for a list
# 'item' in set -> O(1) for a set
