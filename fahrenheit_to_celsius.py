#!/usr/bin/python3

"""
.. moduleauthor:: Deniz Litschauer <deniz.litschi@gmail.com>
"""

f = float(input('Enter a temperature in degrees Fahrenheit: '))

f_to_c = 5/9*(f - 32)

print(f'{f} degrees Fahrenheit correspond to {f_to_c:.2f} degrees Celsius')
