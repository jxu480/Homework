# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

# how many read, how long they are, how big

import sys
import random
import statistics

gensize = int(sys.argv[1])
readnum = int(sys.argv[2])
readlen = int(sys.argv[3])

genome = [0] * gensize

for i in range(readnum):
	index = random.randint(0, gensize - readlen)
	
	for j in range(readlen):
		genome[index +j] += 1
		

print(genome)
print(min(genome[readlen:-readlen]))
print(max(genome[readlen:-readlen]))
print(statistics.mean(genome[readlen:-readlen]))


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
