# This problem was asked by Facebook.
# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

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