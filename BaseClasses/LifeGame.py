#!/usr/bin/env python3
from BaseClasses.Grid import *
import time
import sys


class LifeGame:
    def incrementState(self):
        time.sleep(self.sleepTime)
        self.runTimes += 1
        self.myGrid.getFutureGridState()
        self.myGrid.printGrid()

    @staticmethod
    def _printOriginalGrid(originalGrid):
        print("You said --verbose: this is your grid seed:")
        Grid.printThis(originalGrid, originalGrid.width)

    def runGame(self, verbose):
        originalGrid = self.myGrid.rows
        while (self.maxRunTimes == 0 or self.runTimes < self.maxRunTimes) and \
                self.myGrid.anyAlive() and self.myGrid.notAllAlive():
            try:
                self.incrementState()
            except KeyboardInterrupt:
                if verbose is True:
                    self._printOriginalGrid(originalGrid)
                print("Later Nerd :)")
                break
        if verbose is True:
            self._printOriginalGrid(originalGrid)
        print("NumberOfTurnsRan:", self.runTimes)
        print("Later Nerd :)")


