"This problem was asked by Google."
"You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on."
"Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board."
"For example, given the following board:"
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
"and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row."

class Element:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

def isValid(maze, visited, i, j, M, N):
    return (not (i<0 or j<0 or i >=M or j>=N or maze[i][j] or visited[i][j]))

def findShortestRoute(maze, start, end):
    M = len(maze)
    if M > 0:
        N = len(maze[0])
    else:
        N = 0
    
    visited = []
    for i in range(M):
        visited.append([False]*N)

    elementQueue = []

    if isValid(maze, visited, start[0], start[1], M, N):
        elementQueue.append(Element(start[0], start[1], 0))
        visited[start[0]][start[1]] = True
    else:
        return None


    while len(elementQueue) > 0:
        tempElement = elementQueue.pop(0)

        if tempElement.x == end[0] and tempElement.y == end[1]:
            return tempElement.distance

        # Up
        if isValid(maze, visited, tempElement.x - 1, tempElement.y, M, N):
            elementQueue.append(Element(tempElement.x - 1, tempElement.y, tempElement.distance + 1))
            visited[tempElement.x - 1][tempElement.y] = True
        # Down
        if isValid(maze, visited, tempElement.x + 1, tempElement.y, M, N):
            elementQueue.append(Element(tempElement.x + 1, tempElement.y, tempElement.distance + 1))
            visited[tempElement.x + 1][tempElement.y] = True
        # Left
        if isValid(maze, visited, tempElement.x, tempElement.y - 1, M, N):
            elementQueue.append(Element(tempElement.x, tempElement.y - 1, tempElement.distance + 1))
            visited[tempElement.x][tempElement.y - 1] = True
        # Right
        if isValid(maze, visited, tempElement.x, tempElement.y + 1, M, N):
            elementQueue.append(Element(tempElement.x, tempElement.y + 1, tempElement.distance + 1))
            visited[tempElement.x][tempElement.y + 1] = True
    
    return None
        

    

maze = [[False, False, False, False],
[True, True, False, True],
[False, False, False, False],
[False, False, False, False]]

start = [3, 0]
end = [0, 0]

print(findShortestRoute(maze, start, end))