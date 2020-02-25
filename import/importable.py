def findItem(e, l):
    for i, el in enumerate(l):
        if el == e:
            return [i, el]
    
    return None
