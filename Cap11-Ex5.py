def add_vectors(x,y):
    w = len(x)
    sum = []
    i = 0
    while i < w:
        sum.append(x[i]+y[i])
        i += 1
    return sum

def test(a,b):
    if a == b:
        print ("true")
    else:
        print("false")

sum1 = add_vectors([1,1],[1,1])
sum2 = add_vectors([1, 2], [1, 4])
sum3 = add_vectors([1, 2, 1], [1, 4, 3])

print("test(add_vectors([1, 1], [1, 1]) == [2, 2])")
test(sum1, [2,2])
print("test(add_vectors([1, 2], [1, 4]) == [2, 6]")
test(sum2,[2, 6])
print("test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])")
test(sum3, [2, 6, 4])



