#!/usr/bin/python3

"""
.. moduleauthor:: Deniz Litschauer <deniz.litschi@gmail.com>
"""

rate = float(input('Enter the fixed interest rate in percent: '))

amount = float(input('Enter the amount of money you want to invest: '))

time = int(input('Enter the number of years the money will be invested: '))

final_amount = amount * ( (1 + rate / 100) ** time )

interest = final_amount - amount

print(f'The earned interest is {interest:.2f}.')

print(f'The terminal value amounts to {final_amount:.2f}.')
