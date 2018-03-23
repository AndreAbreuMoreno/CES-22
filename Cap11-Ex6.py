def scalar_mult(a,b):
    sz = len(b)
    i = 0
    scalar = []
    while i < sz:
        scalar.append(a*b[i])
        i += 1
    return scalar

def test(a,b):
    if a == b:
        print("true")
    else:
        print("false")

a = 5
b = [1,2]
c = 3
d = [1, 0, -1]
e = 7
f = [3, 0, 5, 11, 2]

print("test(scalar_mult(5, [1, 2]) == [5, 10]")
mult = scalar_mult(a,b)
test(mult, [5, 10])

print("test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3]")
mult2 = scalar_mult(c,d)
test(mult2,[3, 0, -3])

print("test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]")
mult3 =scalar_mult(e,f)
test(mult3,[21, 0, 35, 77, 14])