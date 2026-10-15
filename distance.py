#!/usr/bin/python3

"""
.. moduleauthor:: Deniz Litschauer <deniz.litschi@gmail.com>
"""

import math

x_coor = float(input("First point's x-coordinate: "))
y_coor = float(input("First point's y-coordinate: "))
x_coor2 = float(input("Second point's x-coordinate: "))
y_coor2 = float(input("Second point's y-coordinate: "))

euclid = math.sqrt((x_coor2 - x_coor) ** 2 + (y_coor2 - y_coor) ** 2)

print(f"The euclidean distance between the two points is {euclid:.4f}.")
