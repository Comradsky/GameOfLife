#!/usr/bin/env python3
from BaseClasses.Grid import *
import asyncio


class GridAsync(Grid):
    async def _getFutureRow(self, y):
        yRow = self.getFutureGridRow(y)
        return yRow

    async def _getFutureRows(self):
        tasks = []
        for row in range(0, self.width + 1):
            tasks.append(asyncio.ensure_future(self._getFutureRow(row)))

        return await asyncio.gather(*tasks)

    def getFutureGridState(self):
        self.rows = asyncio.run(self._getFutureRows())
