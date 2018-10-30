# import copy

class Queue:
    L = []
    def __init__(self):
        print(self.L)
    def enqueue(self,element):
        self.L.append(element)
    def dequeue(self):
        if(self.isEmpty() == False):
            return self.L.pop(0)
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0
################
class Stack:
    L = []
    def __init__(self):
        print(self.L)
    def push(self,element):
        self.L.append(element)
    def pop(self):
        if(self.isEmpty() == False):
            return self.L.pop()
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0
################
class MazeNode:
    # _x = 0
    # _y = 0
    # _isLeft = False
    # _isRight = False
    # _isTop = False
    # _isBottom = False
    def __init__(self, y, x, isLeft, isRight, isTop, isBottom):
        self._x = x
        self._y = y
        self._isLeft = isLeft
        self._isRight = isRight
        self._isTop = isTop
        self._isBottom = isBottom
################
class Maze:
    def __init__(self, xSquare, ySquare):
        self._xSquare = xSquare
        self._ySquare = ySquare
        self._maze = []
        self._startNode = None
        self._goalNode = None
        self.initializeMaze()

    def initializeMaze(self):
        for i in range(self._ySquare):
            row = []
            for j in range(self._xSquare):
                row.append(None)
            self._maze.append(row)

    def setStartNode(self, x, y):
        self._startNode = (x, y)

    def setGoalNode(self, x, y):
        self._goalNode = (x, y)

    def addMazeSquare(self, x, y, isLeft, isRight, isTop, isBottom):
        newMazeSquare = MazeNode(y, x, isLeft, isRight, isTop, isBottom)
        self._maze[y][x] = newMazeSquare

    def getMazeNodeByXY(self, x, y):
        return self._maze[y][x]

    def getMazeNodeByCoords(self, coords):
        return self._maze[coords[1]][coords[0]]

    def getMazeNodeChildren(self, x, y):
        children = []
        if (x > 0 and not self._maze[y][x]._isLeft):
            children.append((self._maze[y][x - 1]._x, self._maze[y][x - 1]._y))
        if (x < (self._xSquare - 1) and not self._maze[y][x]._isRight):
            children.append((self._maze[y][x + 1]._x, self._maze[y][x + 1]._y))
        if (y > 0 and not self._maze[y][x]._isTop):
            children.append((self._maze[y - 1][x]._x, self._maze[y - 1][x]._y))
        if (y < (self._ySquare - 1) and not self._maze[y][x]._isBottom):
            children.append((self._maze[y + 1][x]._x, self._maze[y + 1][x]._y))
        return children

    def depthFirstTraverse(self):
        if (self._startNode is None or self._goalNode is None):
            return None

        stack = Stack()
        stack.push([self._startNode])
        paths = []

        while (not stack.isEmpty()):
            currentPath = stack.pop()
            # print("Current Path", currentPath)
            currentXY = currentPath[-1]
            # print("Current XY", currentXY)
            if (self._goalNode == currentXY):
                paths.append(currentPath)
                # print(paths)
            currentNode = self.getMazeNodeByCoords(currentXY)
            currentChildren = self.getMazeNodeChildren(currentXY[0], currentXY[1])[::-1]
            # print(currentChildren)
            for child in currentChildren:
                # print(child)
                if (child in currentPath):
                    continue
                stack.push(currentPath + [child])
        return paths

    def breadthFirstTraverse(self):
        if (self._startNode is None or self._goalNode is None):
            return None

        queue = Queue()
        queue.enqueue([self._startNode])
        paths = []

        while (not queue.isEmpty()):
            currentPath = queue.dequeue()
            # print("Current Path", currentPath)
            currentXY = currentPath[-1]
            if (self._goalNode == currentXY):
                paths.append(currentPath)
            currentNode = self.getMazeNodeByCoords(currentXY)
            currentChildren = self.getMazeNodeChildren(currentXY[0], currentXY[1])[::-1]
            for child in currentChildren:
                if (child in currentPath):
                    continue
                queue.enqueue(currentPath + [child])
        return paths



##########################
# Main App


# =================================================================================
# =================================================================================
# =================================================================================
# OUR NEW MAZE


our_maze = Maze(10 , 10 )
# (x, y, isLeft, isRight, isTop, isBottom)
# First Row
our_maze.addMazeSquare(0, 0, 1, 0, 1, 0)
our_maze.addMazeSquare(0, 1, 0, 0, 1, 1)
our_maze.addMazeSquare(0, 2, 0, 1, 1, 0)
our_maze.addMazeSquare(0, 3, 1, 0, 1, 0)
our_maze.addMazeSquare(0, 4, 0, 0, 1, 0)
our_maze.addMazeSquare(0, 5, 0, 0, 1, 1)
our_maze.addMazeSquare(0, 6, 0, 0, 1, 1)
our_maze.addMazeSquare(0, 7, 0, 1, 1, 1)
our_maze.addMazeSquare(0, 8, 1, 0, 1, 0)
our_maze.addMazeSquare(0, 9, 0, 1, 1, 0)
# Second Row
our_maze.addMazeSquare( 1 , 0 , 1, 0, 0, 1)
our_maze.addMazeSquare( 1 , 1 , 0, 1, 1,1 )
our_maze.addMazeSquare( 1 , 2 , 1, 1, 0,0)
our_maze.addMazeSquare( 1 , 3 , 1, 1, 0, 0)
our_maze.addMazeSquare( 1 , 4 , 1, 0, 0, 1)
our_maze.addMazeSquare( 1 , 5 , 0, 0, 1, 1)
our_maze.addMazeSquare( 1 , 6 , 0, 0, 1, 1)
our_maze.addMazeSquare( 1 , 7 , 0, 1, 1, 0)
our_maze.addMazeSquare( 1 , 8 , 1,1, 0, 0)
our_maze.addMazeSquare( 1 , 9 , 1, 1, 0,0)
# Third Row
our_maze.addMazeSquare( 2 , 0 , 1, 1, 1, 0)
our_maze.addMazeSquare( 2 , 1 , 1, 0, 1,0 )
our_maze.addMazeSquare( 2 , 2 , 0, 1, 0,1)
our_maze.addMazeSquare( 2 , 3 , 1, 0, 0, 1)
our_maze.addMazeSquare( 2 , 4 , 0, 0, 1, 1)
our_maze.addMazeSquare( 2 , 5 , 0, 1, 1, 0)
our_maze.addMazeSquare( 2 , 6 , 1, 1, 1,0)
our_maze.addMazeSquare( 2 , 7 , 1, 1,0, 0)
our_maze.addMazeSquare( 2 , 8 , 1,1, 0, 0)
our_maze.addMazeSquare( 2 , 9 , 1, 1, 0,0)
# Fourth Row
our_maze.addMazeSquare( 3 , 0 , 1, 1, 0, 0)
our_maze.addMazeSquare( 3 , 1 , 1, 0, 0,1 )
our_maze.addMazeSquare( 3 , 2 , 0, 0, 1,1)
our_maze.addMazeSquare( 3 , 3 , 0, 1, 1, 0)
our_maze.addMazeSquare( 3 , 4 , 1, 0, 1, 0)
our_maze.addMazeSquare( 3 , 5 , 0, 0, 0, 1)
our_maze.addMazeSquare( 3 , 6 , 0, 1,0,0)
our_maze.addMazeSquare( 3 , 7 , 1, 0,0, 0)
our_maze.addMazeSquare( 3 , 8 , 0,1, 0,1)
our_maze.addMazeSquare( 3 , 9 , 1, 1, 0,0)

# Fifth Row
our_maze.addMazeSquare( 4 , 0 , 1, 0, 0, 1)
our_maze.addMazeSquare( 4 , 1 , 0, 0, 1,0 )
our_maze.addMazeSquare( 4 , 2 , 0, 1, 1,1)
our_maze.addMazeSquare( 4 , 3 , 1, 0, 0, 1)
our_maze.addMazeSquare( 4 , 4 , 0, 1, 0, 1)
our_maze.addMazeSquare( 4 , 5 , 1, 0, 1, 0)
our_maze.addMazeSquare( 4 , 6 , 0, 1, 0,1)
our_maze.addMazeSquare( 4 , 7 , 1, 0,0, 1)
our_maze.addMazeSquare( 4 , 8 , 0,1, 1, 1)
our_maze.addMazeSquare( 4 , 9 , 1, 1, 0,0)

# Sixth Row
our_maze.addMazeSquare( 5 , 0 , 1, 1, 1, 0)
our_maze.addMazeSquare( 5 , 1 , 1, 0, 0,1 )
our_maze.addMazeSquare( 5 , 2 , 0, 0, 1,1)
our_maze.addMazeSquare( 5 , 3 , 0, 0, 1, 1)
our_maze.addMazeSquare( 5 , 4 , 0, 0, 1,0)
our_maze.addMazeSquare( 5 , 5 , 0, 1, 0,1)
our_maze.addMazeSquare( 5 , 6 , 1, 1, 1,0)
our_maze.addMazeSquare( 5 , 7 , 1, 0,1, 0)
our_maze.addMazeSquare( 5 , 8 , 0,1, 1, 0)
our_maze.addMazeSquare( 5 , 9 , 1, 0, 0,0)

# Seventh Row
our_maze.addMazeSquare( 6 , 0 , 1, 0, 0, 1)
our_maze.addMazeSquare( 6 , 1 , 0, 0, 1,1 )
our_maze.addMazeSquare( 6 , 2 , 0, 0, 1,0)
our_maze.addMazeSquare( 6 , 3 , 0, 1,1, 1)
our_maze.addMazeSquare( 6 , 4 , 1, 1, 0, 0)
our_maze.addMazeSquare( 6 , 5 , 1, 0, 1, 0)
our_maze.addMazeSquare( 6 , 6 , 0, 0, 0,1)
our_maze.addMazeSquare( 6 , 7 , 0, 1,0, 0)
our_maze.addMazeSquare( 6 , 8 , 1,0, 0, 1)
our_maze.addMazeSquare( 6 , 9 , 0, 1, 0,1)

# Eighth Row

our_maze.addMazeSquare( 7 , 0 , 1, 0, 1, 0)
our_maze.addMazeSquare( 7 , 1 , 0, 0, 1,1 )
our_maze.addMazeSquare( 7 , 2 , 0, 0, 0,1)
our_maze.addMazeSquare( 7 , 3 , 0, 0, 1, 1)
our_maze.addMazeSquare( 7 , 4 , 0, 1, 0, 1)
our_maze.addMazeSquare( 7 , 5 , 1, 0, 0, 0)
our_maze.addMazeSquare( 7 , 6 , 0, 1, 1,0)
our_maze.addMazeSquare( 7 , 7 , 1, 1,0, 0)
our_maze.addMazeSquare( 7 , 8 , 1,0, 1, 1)
our_maze.addMazeSquare( 7 , 9 , 0, 1, 1,0)

# Ninth Row
our_maze.addMazeSquare( 8 , 0 , 1, 1, 0, 1)
our_maze.addMazeSquare( 8 , 1 , 1, 0, 1,0 )
our_maze.addMazeSquare( 8 , 2 , 0, 0, 1,1)
our_maze.addMazeSquare( 8 , 3 , 0, 0, 1, 0)
our_maze.addMazeSquare( 8 , 4 , 0, 1, 1, 0)
our_maze.addMazeSquare( 8 , 5 , 1, 1, 0, 0)
our_maze.addMazeSquare( 8 , 6 , 1, 1, 0,0)
our_maze.addMazeSquare( 8 , 7 , 1, 0,0, 1)
our_maze.addMazeSquare( 8 , 8 , 0,0, 1, 1)
our_maze.addMazeSquare( 8 , 9 , 0, 1, 0,1)

# Tenth Row
our_maze.addMazeSquare( 9 , 0 , 0, 0, 1,1)
our_maze.addMazeSquare( 9 , 1 , 0, 1, 0,1 )
our_maze.addMazeSquare( 9 , 2 , 1, 0, 1,1)
our_maze.addMazeSquare( 9 , 3 , 0, 1, 0, 1)
our_maze.addMazeSquare( 9 , 4 , 1, 0, 0, 1)
our_maze.addMazeSquare( 9 , 5 , 0, 1, 0, 1)
our_maze.addMazeSquare( 9 , 6 , 1, 0, 0,1)
our_maze.addMazeSquare( 9 , 7 , 0, 0,1, 1)
our_maze.addMazeSquare( 9 , 8 , 0,0, 1, 1)
our_maze.addMazeSquare( 9 , 9 , 0, 1, 1,1)


our_maze.setStartNode(5, 9)
our_maze.setGoalNode(9, 0)

print("Using Depth First : ")
print(our_maze.depthFirstTraverse())
print("\n")
print("Using Breadth First : ")
print(our_maze.breadthFirstTraverse())
