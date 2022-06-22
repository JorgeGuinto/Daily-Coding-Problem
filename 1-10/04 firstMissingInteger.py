#Brute Force
def firstMisingInteger(x):
    x = merge_sort(x)
    for k in range(len(x) - 1):
        m = x[k]
        if m < 1:
            continue
        else:
            j = k
            break
        
    i = 1
    while i < len(x) and j < len(x):
        if i == x[j]:
            i += 1
            j += 1
            continue
        elif i < x[j]:
            return i
        else:
            j += 1
    return x[len(x)-1] + 1
    
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

x = [3, 4, -1, 1, 2, 0, -2, -3, -5, 5]
y = [1, 2, 0]
print(firstMisingInteger(x))