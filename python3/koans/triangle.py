#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

from itertools import combinations


def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    #if a == b:
    #    if b == c:
    #        return 'equilateral'
    #    else:
    #        return 'isosceles'
    #elif b == c:
    #    return 'isosceles'

    #elif a == c:
    #    return 'isosceles'

    #else:
    #    return 'scalene'

    if not a + b > c or not a + c > b or not b + c > a:
        raise TriangleError

    num = [x == y for x, y in combinations((a, b, c), 2)].count(True)

    if num == 0:
        return 'scalene'
    elif num == 1:
        return 'isosceles'
    elif num == 3:
        return 'equilateral'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
