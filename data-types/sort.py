li = [10, 3, 2, 6, 12, 43, 22, 12, 52, 8]

# Creating a new variable
sLi = sorted(li, reverse=True)
print(sLi)

# or
li.sort()
print(li)

# Sorted is preferred due to the fact that it works on other data types
# Other examples

newLi = [-2, -6, 3, 4, 1, 5]
newLiSorted = sorted(newLi, key=abs)
print(newLiSorted)