# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import sys
import math

arr = []
sum = 0.0
tot = 0.0

for val in sys.argv[1:]:
	arr.append(float(val))
	arr.sort()

for i in range(len(arr)):
	tot += arr[i]
	
if tot != 1.0:
	print('Error: Does not sum to 1.0')	
else:
	for i in range(len(arr)):
		val = arr[i]
		sum += (val * math.log2(val))

	sum *= -1

	print(f'{sum:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
