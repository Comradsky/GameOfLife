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

    def runGame(self):
        while (self.maxRunTimes == 0 or self.runTimes < self.maxRunTimes) and \
                self.myGrid.anyAlive() and self.myGrid.notAllAlive():
            try:
                self.incrementState()
            except KeyboardInterrupt:
                print("Later Nerd :)")
                break
        print("NumberOfTurnsRan:", self.runTimes)

