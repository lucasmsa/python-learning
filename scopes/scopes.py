# Global variable x
x = 'global -> x'

def test():
    # To use the global var, not recommended
    # global x
    x = 'local -> x'
    y = 'local -> y'
    print(x + " - " + y)


def outer():
    x = 'outer x'
    
    def inner():
        # To access the outer x
        # nonlocal x
        x = 'inner x'


test()

