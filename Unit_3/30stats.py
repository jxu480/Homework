# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

list = []
count = 0
min = 0
max = 0
total = 0

for val in sys.argv[1:]:
	list.append(float(val))
	list.sort()
	count += 1
	if float(val) > max:
		max = float(val)
	
	if min == 0:
		min = float(val)
	elif float(val) < min:
		min = float(val)
	
	total += float(val)

mean = total/count

sum = 0
for val in sys.argv[1:]:
	sum += (float(val) - mean)**2

median = list[int(len(list) / 2)]
std = (sum / count)**0.5

print(list)
print(f'Count: {count}', f'Minimum: {min}', f'Maximum: {max}', f'Mean: {mean:.3f}',
 f'Std. dev: {std:.3f}', f'Median: {float(median):.3f}' ,sep='\n')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
