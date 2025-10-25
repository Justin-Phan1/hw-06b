# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(7,8,9),'Scalene')
        self.assertEqual(classifyTriangle(5,4,3),'Scalene')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(5,5,6),'Isoceles')

    def testInvalidInputs(self): 
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput') # sides greater than 200
        self.assertEqual(classifyTriangle(3,3,0),'InvalidInput') # side length of 0
        self.assertEqual(classifyTriangle(3,4,False),'InvalidInput') # invalid type bool instead of int

    def testNotTriangle(self): 
        self.assertEqual(classifyTriangle(7,2,3),'NotATriangle') # a >= (b + c) 
        self.assertEqual(classifyTriangle(2,6,3),'NotATriangle') # b >= (a + c)
        self.assertEqual(classifyTriangle(2,4,8),'NotATriangle') # c >= (a + b)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

