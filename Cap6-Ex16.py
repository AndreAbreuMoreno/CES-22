def is_factor(x,y):
    if y%x == 0:
        return True
    else:
        return False

def test(x,y):
    if is_factor(x,y) == True:
        print("is_factor({},{})".format(x,y))
    else:
        print("not is_factor({},{})".format(x,y))

test(3,12)
test(5,12)
test(7,14)
test(7,15)
test(1,15)
test(15,15)
test(25,15)