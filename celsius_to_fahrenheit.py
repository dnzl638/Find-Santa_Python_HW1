#!/usr/bin/python3

"""
.. moduleauthor:: Deniz Litschauer <deniz.litschi@gmail.com>
"""

c = -15

while c >= -15 and c <= 35:

    c_to_f = (9 / 5) * c + 32

    print(f'{c} C => {c_to_f:.1f} F')

    c += 1
