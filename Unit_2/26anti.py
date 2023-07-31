# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

cdna = ''
rdna = ''

for i in range(len(dna)):
	if dna[i] == 'A':
		cdna += 'T'
	elif dna[i] == 'C':
		cdna += 'G'
	elif dna[i] == 'G':
		cdna += 'C'
	else:
		cdna += 'A'

for i in range(len(cdna)):
	rdna += cdna[len(cdna)- 1 - i]
	
print(rdna)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
