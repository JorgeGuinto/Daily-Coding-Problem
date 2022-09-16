
def paintingHouses(matrix):
    
    n = len(matrix)
    k = len(matrix[0])
    cost = [[0] * k]

    for r, row in enumerate(matrix):
        rowCost = []
        for c, value in enumerate(row):
            rowCost.append(min(cost[r][i]
                                for i in range(k)
                                if i != c) + value)
        cost.append(rowCost)
    return min(cost[-1])


def buildingHouses(matrix):

    k = len(matrix[0])
    cost = [0] * k

    for r, row in enumerate(matrix):
        rowCost = []
        for c, value in enumerate(row):
            rowCost.append(min(cost[i]
                                for i in range(k)
                                if i != c) + value)
        cost = rowCost
    return min(cost)

matrix = [[5, 6, 1], [1, 11, 6], [7, 2, 8]]
print(paintingHouses(matrix))
print(buildingHouses(matrix))