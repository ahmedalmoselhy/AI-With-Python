import copy

class queue:
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
class stack:
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
    def __init__(self, x, y, isLeft, isRight, isTop, isBottom):
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

    
