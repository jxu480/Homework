# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
import math

list = []

for val in sys.argv[1:]:
	list.append(int(val))
	
days = list[0]
people = list[1]

a = math.factorial(days)/math.factorial(days - people)
b = days ** people

prob = a/b

print(f'{1-prob:.3f}')

"""
python3 33birthday.py 365 23
0.571
"""

