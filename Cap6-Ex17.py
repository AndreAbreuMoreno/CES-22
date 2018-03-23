def is_factor(x,y):
    if y%x == 0:
        return True
    else:
        return False

def is_multiple(x,y):
    return is_factor(y,x)

def test(x,y):
    if is_multiple(x,y) == True:
        print("is_multiple({},{})".format(x,y))
    else:
        print("not is_factor({},{})".format(x,y))

test(12,3)
test(12,4)
test(12,5)
test(12,6)
test(12,7)



