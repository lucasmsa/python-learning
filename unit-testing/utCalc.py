# unit testing is used for testing functions in the code


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2  

def divide(n1, n2):
    try:
        return n1 / n2
    except (ValueError):
        print('cannot divide by zero')