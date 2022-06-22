import numbers
from operator import indexOf
#file = open("03 IntegerArray.txt","r")
#x = file.read().splitlines()

def merge(a, b):
    c = []
    i = 0
    j = 0
    
    while i < len(a) and j < len(b):
        c.append(min(a[i], b[j]))
        if b[j] < a[i]:
            j += 1
        else:
            i += 1

    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])

    return c

def merge_sort(x):
    if len(x) == 1:
        return x
    else:
        a = x[0:int(len(x)/2)]
        b = x[int(len(x)/2):len(x)]
        a = merge_sort(a)
        b = merge_sort(b)
        s = merge(a,b)
    return s

#w = merge_sort(x)
#print(w)


a = [5, 10, 15, 20]
b = [3, 6, 9, 12]
c = [2, 4, 8, 14]
d = [1, 7, 13, 21]

t = [a, b, c, d]

def join_arrays (x):
    z = x[0]    
    for k in range(len(x)-1):
        z = merge(z,x[k+1])
    return z

print(join_arrays(t))