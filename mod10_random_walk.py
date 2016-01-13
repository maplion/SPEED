#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 10: Random Walk

Models the walking of random walkers.

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

from matplotlib.pylab import *
import speedcalc

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

# s_cli = speedcli.SpeedCLI(description="SPEED Random Walk")

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """
    This is the main function for Module 10
    """

    try:
        # Declare local main Variables
        if argv is None:
            argv = sys.argv
        numberOfDimensions = 1
        numberOfRandomWalkers = int(argv[1])
        numberOfSteps = int(argv[2])
        averageStepSize = float(argv[3])
        stdInStepSize = float(argv[4])
        beginningPosition = float(argv[5])
        if len(argv) == 7:
            numberOfDimensions = int(argv[6])

        sc_rw = speedcalc.RandomWalk(numberOfRandomWalkers, numberOfSteps, averageStepSize, stdInStepSize,
                                     beginningPosition)

        if numberOfDimensions > 1:
            x_values, y_values = sc_rw.randomWalk_2D()

            # Plots
            plot(x_values, y_values, 'bo')
            xlabel('Steps (East/West)')
            ylabel('Steps (North/South)')
            title('Ryan Dammrose Module 10: Random Walking')
            # savefig(outputFilePath, dpi=300)
            show()
        else:
            totalSummed, averageSteps = sc_rw.random_walk_1d()

            # Plots
            for walkers in range(numberOfRandomWalkers):
                plot(totalSummed[:, walkers])
                hold('on')
            plot(averageSteps, 'k-', linewidth=4)
            xlabel('Step Interval')
            ylabel('Number of steps from origin')
            title('Ryan Dammrose Module 10: Random Walking')
            # savefig(outputFilePath, dpi=300)
            show()

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
