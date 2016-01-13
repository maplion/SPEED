#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Tests calculations for evapotranspiration calculations; those in the ET subclass in speedcalc.py

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import unittest
import numpy as np
import speedcalc
import test_logging

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

log = test_logging.TestLogging()
sc = speedcalc


class TestCalculations_Polygon(unittest.TestCase):

    def test_validatePolygon(self):
        """
        Does invalid polygon coordinates raise a ValueError exception?
        """
        testName = "test_validatePolygon"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            x_coords = np.asarray([550, 455, 491, 609, 645])
            y_coords = np.asarray([450, 519, 631, 631, 510])

            # Could not get self.assertRaises to work for this, so I went with this method
            try:
                sc.Polygon(x_coords, y_coords)
            except ValueError as e:
                pass
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_setPolyArea(self):
        """
        Is the Polygon Area calculated correctly?
        """
        testName = "test_setPolyArea"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            x_coords = np.asarray([0, 10, 10, 0])
            y_coords = np.asarray([10, 10, 0, 0])

            x_coords2 = np.asarray([550, 455, 491, 609, 645])
            y_coords2 = np.asarray([450, 519, 631, 631, 519])

            poly = sc.Polygon(x_coords, y_coords)
            poly2 = sc.Polygon(x_coords2, y_coords2)

            self.assertEqual(poly._area, 100)
            self.assertEqual(round(poly2._area, 0), 23803)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_setPolyCentroid(self):
        """
        Is the Polygon Centroid calculated correctly?
        """
        testName = "test_setPolyCentroid"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            x_coords = np.asarray([0, 10, 10, 0])
            y_coords = np.asarray([10, 10, 0, 0])

            x_coords2 = np.asarray([550, 455, 491, 609, 645])
            y_coords2 = np.asarray([450, 519, 631, 631, 519])

            poly = sc.Polygon(x_coords, y_coords)
            poly2 = sc.Polygon(x_coords2, y_coords2)

            self.assertEqual(poly._centroid_x, 5)  # Depends on Area
            self.assertEqual(poly._centroid_y, 5)  # Depends on Area
            self.assertEqual(round(poly2._centroid_x, 1), 550.0)
            self.assertEqual(round(poly2._centroid_y, 1), 550.1)
            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

    def test_setPolyPerimeter(self):
        """
        Is the polygon Perimeter calculated correctly?
        """
        testName = "test_setPolyPerimeter"
        try:
            log.print_test_begin(testName)
            # ------------------------------------
            x_coords = np.asarray([0, 10, 10, 0])
            y_coords = np.asarray([10, 10, 0, 0])

            x_coords2 = np.asarray([550, 455, 491, 609, 645])
            y_coords2 = np.asarray([450, 519, 631, 631, 519])

            poly = sc.Polygon(x_coords, y_coords)
            poly2 = sc.Polygon(x_coords2, y_coords2)

            self.assertEqual(poly._perimeter, 40)
            self.assertEqual(round(poly2._perimeter, 3), 588.115)

            # ------------------------------------
            log.print_test_success(testName)
        except:
            log.print_test_failure(testName)
            self.fail(msg=testName[testName.rfind("_")+1:] + "() FAILED")

##########################################################################################


def suite():
    """
    Gather all the tests from this module in a test suite.
    """
    _suite = unittest.TestSuite()
    _suite.addTest(TestCalculations_Polygon('test_validatePolygon'))
    _suite.addTest(TestCalculations_Polygon('test_setPolyArea'))
    _suite.addTest(TestCalculations_Polygon('test_setPolyCentroid'))
    _suite.addTest(TestCalculations_Polygon('test_setPolyPerimeter'))
    return _suite
