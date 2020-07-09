#!/usr/bin/env python3
from BaseClasses.LifeGame import *
from Logic.GridSynchronous import *


class LifeGameSync(LifeGame):
    def __init__(self, dimensionSize, chancePercent, maxRunTimes, sleepTime):
        self.myGrid = GridSync(dimensionSize, chancePercent)
        self.maxRunTimes = maxRunTimes
        self.sleepTime = sleepTime
        self.runTimes = 0


def startSyncGame(dimensionSize, chancePercent, maxRunTimes, sleepTime, verbose):
    gameOfLife = LifeGameSync(dimensionSize, chancePercent, maxRunTimes, sleepTime)
    gameOfLife.runGame(verbose)
