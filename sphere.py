#!/usr/bin/python3

"""
.. moduleauthor:: Deniz Litschauer <deniz.litschi@gmail.com>
"""

from math import pi
r = float(input("Enter a radius: "))
area = 4 * r**2 * pi
volume = (4 / 3) * r**3 * pi
print("The sphere has a volume of", round(volume, 2));
print("The surface area of this sphere is", round(area, 2));
