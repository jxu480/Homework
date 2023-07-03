# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random

nts = ''
num = 0

for i in range(30):
	a = random.random()
	if a >= 0.4:
		nts += random.choice('AT')
		num += 1
	else:
		nts += random.choice('GC')

print(len(nts), num/len(nts), nts)


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
