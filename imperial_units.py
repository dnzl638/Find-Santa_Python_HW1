# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

meter = float(input('Enter a distance in meters: '))

inch = meter * 39.37
foot = inch / 12
yard = foot / 3
mile = yard / 1760

print(f'{inch:.2f} inch')
print(f'{foot:.2f} feet')
print(f'{yard:.2f} yards')
print(f'{mile:.2f} miles')

