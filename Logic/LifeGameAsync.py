#!/usr/bin/env python3
from BaseClasses.LifeGame import *
from Logic.GridAsynchronous import *


class LifeGameAsync(LifeGame):
    def __init__(self, dimensionSize, chancePercent, maxRunTimes, sleepTime):
        self.myGrid = GridAsync(dimensionSize, chancePercent)
        self.maxRunTimes = maxRunTimes
        self.sleepTime = sleepTime
        self.runTimes = 0


def startAsyncGame(dimensionSize, chancePercent, maxRunTimes, sleepTime):
    gameOfLife = LifeGameAsync(dimensionSize, chancePercent, maxRunTimes, sleepTime)
    gameOfLife.runGame()
