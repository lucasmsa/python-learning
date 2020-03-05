# lists are iterable but not iterators
# normal iterable data structure
nums = [1, 2, 3, 4]

# creating an iterator based on the list
iterator_nums = iter(nums)
# or
# iterator_nums = nums.__iter__()


# it will remember the last iteration, and if you surpass the length
# an error will be thrown
# ideally do that inside a loop
# print(next(iterator_nums))
# print(next(iterator_nums))

while True:
    try:
        print(next(iterator_nums))

    except StopIteration:
        break

print(f"dir() for iterator: {dir(iterator_nums)}\n")


# all double underscore (dunder) methods in the nums list
# lists do not have dunder next method, they are not iterators 
print(f"\ndir() for list: {dir(nums)}")
