def squareNumbers(n):
    # Normal function
    result = []
    for i in n:
        result.append(i*i)
    return result

def SquareNumbersGen(n):
    for i in n:
        yield (i*i)

print(squareNumbers([1, 2, 3, 4, 5]))

# The result will be a generator object
numGen = SquareNumbersGen([1, 2, 3, 4, 5])
print(numGen)

print(f'next: {next(numGen)}')
print(f'next: {next(numGen)}')
print(f'netx: {next(numGen)}')


# It doesn't hold the entire result in memory, it yields, the
# results one at a time
for n in numGen:
    # It continues from the last iteration
    print(f'for: {n}')


# Generator comprehension, same as SquareNumbersGen function
myGen = (n*n for n in [1, 2, 3, 4, 5])

# It is possible to print a generator as a list, but you will loose performance
# In a large set of data generators excel in time efficiency
# print(list(myGen))

