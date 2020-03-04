# a way of treating errors

# file doesn't exist, will throw an error
# antecipate parts of code that are prone to errors


try:
    t = open('text.txt')
    o = open('corrupt.txt')
    if o.name == 'corrupt.txt':
        raise Exception
    #var = non_var

# specific file not found case
# more specific at the top
# more general ones the further you go down
except FileNotFoundError as f:
    print('file non-existent. Error -> ' + str(f))
except Exception as e:
    print('something is wrong. Error -> ' + str(e))
# No exceptions thrown
else:
    print(t.read())
    t.close()
# Runs no matter what happens
finally:
    print("Executing finally statement")


# generally better to try and except instead of concatenating conditions in an if statement
# concept related to Duck Typing and Asking Forgiveness, Not Permission - Pythonic way

nums = [1, 2, 3, 4, 5, 6]

# Non-pythonic
if len(nums) >= 6:
    print(nums[5])
else:
    print("Index doesn't exist")


# Pyhtonic
try:
    print(nums[6])
except IndexError as ie:
    print("Index doesn't exist " + str(ie))