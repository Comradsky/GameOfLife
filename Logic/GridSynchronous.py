#!/usr/bin/env python3
from BaseClasses.Grid import *


class GridSync(Grid):
    def getFutureGridState(self):
        nextGridState = []
        for y in range(0, self.width + 1):
            yRow = self.getFutureGridRow(y)
            nextGridState.append(yRow)
        self.rows = nextGridState
