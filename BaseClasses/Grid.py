#!/usr/bin/env python3
import random
import os


class Grid:
    def __init__(self, dimensionSize, chancePercent):
        self.rows = self.randomGrid(dimensionSize, chancePercent)
        self.width = dimensionSize - 1

    @staticmethod
    def randomGrid(dimensionSize, chancePercent):
        grid = []
        for y in range(0, dimensionSize):
            yRow = []
            for x in range(0, dimensionSize):
                chance = random.randint(0, 100)
                if chance <= chancePercent:
                    yRow.append(True)
                else:
                    yRow.append(False)

            grid.append(yRow)
        return grid

    # need a non self based method to print out stored original seed and custom grid objects
    @staticmethod
    def printThis(grid, width):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("▃▃"*width)
        for yRow in grid:
            row = ""
            for x in yRow:
                if x:
                    row += "O "
                else:
                    row += "  "
            print(row)

    # not used right now, this is useful for testing, also displayCounts looks cool
    def displayCounts(self):
        countGrid = []
        for y in range(0, self.width + 1):
            yRow = []
            for x in range(0, self.width + 1):
                yRow.append(self.getNumberOfLiveNeighbors(x, y))
            countGrid.append(yRow)
        self.printThis(countGrid, self.width)

    def printGrid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("▃▃"*self.width)
        for yRow in self.rows:
            row = ""
            for x in yRow:
                if x:
                    row += "O " #░░
                else:
                    row += "  " #░░
            print(row)

    def anyAlive(self):
        for yRow in self.rows:
            if any(yRow):
                return True
        return False

    def notAllAlive(self):
        for yRow in self.rows:
            if not all(yRow):
                return True
        return False

    def getNumberOfLiveNeighbors(self, x, y):
        liveCount = 0
        for k in range(-1, 2):
            if not (y + k in range(0, self.width)):
                continue
            for j in range(-1, 2):
                if not (x + j in range(0, self.width)):
                    continue
                if self.rows[y + k][x + j] is True:
                    liveCount += 1
        return liveCount - self.rows[y][x]

    def getFutureGridRow(self, y):
        yRow = []
        for x in range(0, self.width + 1):
            xVal = False
            liveNeighbors = self.getNumberOfLiveNeighbors(x, y)
            if self.rows[y][x] is True and 2 <= liveNeighbors <= 3:
                xVal = True
            elif self.rows[y][x] is False and liveNeighbors >= 3:
                xVal = True
            yRow.append(xVal)
        return yRow

    def getFutureGridState(self):
        raise NotImplementedError
