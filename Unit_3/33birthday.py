# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

# make the problem smaller (4 people, 20 days)

import random
import math

list = []

# make a list of the calendar
# enter the birthdays of everyone
# 4 people, 20 days

days = 365
people = 23
trials = 100000
success = 0

for a in range(trials):
	calendar = [0] * days
	same = 0
	
	for i in range(people):
		birthday = random.randint(0, days-1)
	
		calendar[birthday] += 1

	for j in range(len(calendar)):
		if calendar[j] > 1:
			same += 1
		
	if same > 0:
		success += 1

print(success / trials)


"""
python3 33birthday.py 365 23
0.571
"""

