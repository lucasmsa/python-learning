class My_Iter:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    # iter methods have to return iterators
    def __iter__(self):
        return self

    # the iterator class must have a dunder __next__ method
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        currentValue = self.value
        self.value += 1
        return currentValue


nums_it = My_Iter(1, 5)

while True:
    try: 
        print(next(nums_it))

    except StopIteration:
        break

# also works as

#for n in nums_it:
#    print(n)


# generators act like easy to read iterators 
# yielding a value instead of returning it
# keeping the state until the generator runs the next state
def my_gen(start, end):
    
    for i in range(start, end):

        currentValue = start
        start += 1
        yield currentValue

gen = my_gen(1, 10)
print('gen')
for n in gen:
    print(n)

dollynho = 'eh do caralho enfia um pastelao no cu'
