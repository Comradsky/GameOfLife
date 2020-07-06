#!/usr/bin/env python3
from Logic.LifeGameAsync import *
from Logic.LifeGameSync import *


def startTheGame(args):
    if args.runAsyncVersion:
        startAsyncGame(args.dimensionSize, args.chancePercent, args.maxRunTimes, args.sleepTime)
    else:
        startSyncGame(args.dimensionSize, args.chancePercent, args.maxRunTimes, args.sleepTime)


def main(argv):
    from argparse import ArgumentParser
    parser = ArgumentParser(description="""
    Run Conway's Game of Life
    """)
    parser.add_argument('dimensionSize', type=int, help='width of grid')
    parser.add_argument('chancePercent', type=int, help='larger number starts with more live cells')
    parser.add_argument('--runAsyncVersion', action='store_true',
                        help='put True to run Async Logic Version, False to run Synchronous Version (default False)')
    parser.add_argument('--maxRunTimes', default=0, type=int,
                        help='0 for forever, otherwise max number of turns (default 0)')
    parser.add_argument('--sleepTime', default=0.1, type=float,
                        help='number of seconds to sleep between turns (default 0.1)')
    parser.add_argument('--verbose', action='store_true', help='more output')

    parser.set_defaults(func=startTheGame)

    args = parser.parse_args(argv)

    if 'func' in args:
        return args.func(args)
    parser.print_help()
    return -1


if __name__ == '__main__':
    main(sys.argv[1:])
