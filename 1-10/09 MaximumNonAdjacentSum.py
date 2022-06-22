"Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative."
"For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5."

#First Approach
def findMaximumNonAdjacentSum (a):
    size = len(a)
    sumas = [None] * size
    sumas[size - 1] = a[size - 1]
    sumas[size - 2] = max(a[size - 1], a[size - 2])
    
    for i in range(size -3, -1, -1):
        sumas[i] = max(a[i] + sumas[i+2], sumas[i+1])

    return sumas[0]

#Second Approach
def maximumNonAdjacentSum (a):
    size = len(a)
    temp2 = a[size - 1]
    temp1 = max(a[size - 1], a[size - 2])
    temp = 0

    for i in range(size -3, -1, -1):
        temp = max(a[i] + temp2, temp1)
        temp2 = temp1
        temp1 = temp

    return temp


x = [2, 4, 6, 2, 5]
y = [5, 1, 5, 4, 3, 5, 6, 5]
z = [5, 1, 1, 5]

print(findMaximumNonAdjacentSum(z))
print(maximumNonAdjacentSum(x))
print(maximumNonAdjacentSum(y))
print(maximumNonAdjacentSum(z))