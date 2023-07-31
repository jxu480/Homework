# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n = 5 # use this value for your computation

s = 0
f = 1

for i in range(1, n + 1):
	s += i
	f *= i
	
print(n, s, f)

"""
python3 22sumfac.py
5 15 120
"""
