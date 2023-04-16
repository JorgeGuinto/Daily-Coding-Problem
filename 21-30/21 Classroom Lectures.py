def findMinRooms(array):
    if array == None:
        return 0
    if len(array) == 1:
        return 1
    
    array.sort()
    classRoom = [None]*len(array)
    n = 1
    classRoom[0] = (1, 0)

    for i in range(1, len(array)):
        for j in range(0, i):
            blocked = []
            if (array[i][0] > array[j][1] or array[i][1] < array[j][0]) and (blocked.count(classRoom[j][0]) == 0):
                separation = max((array[i][0] - array[j][1]), array[j][0] - array[i][1])
                if classRoom[i] == None or classRoom[i][1] > separation:
                    classRoom[i] = (classRoom[j][0], separation)
            else:
                if j == i-1 and classRoom[i] == None:
                    n += 1
                    classRoom[i] = (n, 0)
                else:
                    blocked.append(classRoom[j][0])
    
    return n
                

x = [(0,50), (60,150), (30,75)]
#print(findMinRooms(x))

y = [(0,50), (30,75), (60,150), (10,87), (100,120), (40,80), (150,200)]
print(findMinRooms(y))