# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

p = 0

for i in range(len(dna)):
	if dna[i] == 'C' or dna[i] == 'G':
		p += 1

print(f'{p / len(dna):.2}')

"""
python3 24gc.py
0.42
"""
