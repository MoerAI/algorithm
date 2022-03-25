import math

def issquare1(n):
    if int(n ** 0.5) ** 2 == n:
        return True
    else:
        return False



def issquare2(n):
    square = math.sqrt(n)
    if int(square) == square:
        return True
    else:
        return False


# issquare1(1)
# issquare2(25)
# issquare1(89011483755109777)