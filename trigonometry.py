# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import math

print(f'{"radians":>7} | {"sine":>5} | {"tangent":>7}')
print('-------------------------')

values = []
start = 0.0

while start < math.pi:
	values.append(start)
	start += 0.1

values.append(math.pi)

for val in values:

	rad = round(val, 2)
	sin = round(math.sin(val), 2)
	tan = round(math.tan(val), 2)

	print(f"{rad:>7} | {sin:>5} | {tan:>7}")
