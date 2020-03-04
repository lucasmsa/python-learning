from collections import namedtuple

# normal tuples
color = (55, 120, 240)
print(color[0])

# nametuples add readability and the functionality of a tuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(blue=55, green=120, red=255)
# or
whiteColor = Color(255,255,255)


print(color.red)
