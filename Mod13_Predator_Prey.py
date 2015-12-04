#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 13: Predator and Prey calculations using Lotka–Volterra equations

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import time
from matplotlib.pylab import *
# import timeit
import speedcalc
import speedloader
# import speedcli

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sl_dc = speedloader.CSV()
# s_cli = speedcli.SpeedCLI(description="SPEED")
# total_time = timeit.timeit('[v for v in range(10000)]', number=10000)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def plotResults(N1, N2, N1_initial, N2_initial, totalTime, timeSteps, dataPoints):
    """
    :return:
    """
    # Plot results for Predator and Prey
    figure(num=None, figsize=(15, 8), dpi=80, facecolor='w', edgecolor='k')
    hold()
    plot(dataPoints, N1, 'r-', dataPoints, N2, 'b-')
    title('Predator and Prey Relationship\n'
          'Total Time: {0}, Time Steps: {1}, Initial Prey: {2}, Initial Predator: {3}\n'.format(totalTime,
        timeSteps, N1_initial, N2_initial))
    xlabel('Time Units')
    ylabel('Population')
    legend(['Prey', 'Predator'])
    show()

def main(argv=None):
    """
    This is the main function for Module 13

    @param argv: incoming arguments
    @return: void
    """

    start_time = time.clock()
    # Declare local main Variables
    # if argv is None:
    #     argv = sys.argv

    try:
        # arguments = s_cli.argParse(argv)

        # get File
        # if arguments.file is None:
        #     sys.exit("No file name given.")
        # if arguments.file2 is None:
        #     sys.exit("No file name given for second file")
        # else:
        #     filename = arguments.inputFilePath + "/" + arguments.file
        #     if ".csv" not in filename:
        #         filename += ".csv"
        #     filename2 = arguments.inputFilePath + "/" + arguments.file2
        #     if ".csv" not in filename2:
        #         filename2 += ".csv"

        # Set Birth Rate and Death Rate variables
        prey_alpha = 0.1
        prey_beta = 0.02
        predator_gamma = 0.4
        predator_delta = 0.02

        sc_pp = speedcalc.PredatorPrey(prey_alpha, prey_beta, predator_gamma, predator_delta)
        # sc_pp_2 = speedcalc.PredatorPrey(prey_alpha, prey_beta, predator_gamma, predator_delta)

        # Set Initial Population, time and time step variables
        N1_initial_1 = 10
        N2_initial_1 = 10
        totalTime_1 = 200
        timeSteps_1 = 1000
        N1_1, N2_1, dataPoints_1 = sc_pp.Lotka_Volterra(N1_initial_1, N2_initial_1, totalTime_1, timeSteps_1)

        # Set Different Initial Population, time and time step variables
        N1_initial_2 = 50
        N2_initial_2 = 30
        totalTime_2 = 300
        timeSteps_2 = 1000
        N1_2, N2_2, dataPoints_2 = sc_pp.Lotka_Volterra(N1_initial_2, N2_initial_2, totalTime_2, timeSteps_2)

        plotResults(N1_1, N2_1, N1_initial_1, N2_initial_1, totalTime_1, timeSteps_1, dataPoints_1)
        plotResults(N1_2, N2_2, N1_initial_2, N2_initial_2, totalTime_2, timeSteps_2, dataPoints_2)

        # Benchmarking
        # print "Single Execution Time: {0} seconds".format(round(execution_time, 6))
        # print "Total wall-clock time to execute the statement 10000 times: {0}".format(total_time)
        # print "Average time per loop: {0}".format(total_time/10000)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
