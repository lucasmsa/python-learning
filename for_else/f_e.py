listEx = [1, 2, 3, 4, 5]

# same for while and for loops
# the else should actually be called noBreak
# it will run if the loop doesn't breakm
for n in listEx:

    print(n)
    if n == 4:
        break

else:
    print('Reached For/Else statement')


def find_index(listEx, element):

    for i, e in enumerate(listEx):
        if e == element:
            break
    # if the for does not break it will trigger this else statement
    else:
        print('Item not found')
        return -1

    return e


print(find_index(listEx, 2))

    