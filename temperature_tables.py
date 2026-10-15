#!/usr/bin/python3

"""
.. moduleauthor:: Deniz Litschauer <deniz.litschi@gmail.com>
"""

cel = -20
fah = -10

choice = input("For C => F enter C, for F => C enter F: ").upper()

if choice == "C":
    for cel in range(-20, 41):

        c_to_f = (9 / 5) * cel + 32

        print(f'{cel} C => {c_to_f:.1f} F')

if choice == "F":
    for fah in range(-10, 111):

        f_to_c = 5 / 9 * (fah - 32)

        print(f'{fah} F => {f_to_c:.1f} C')

else:
    print("")
