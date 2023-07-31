# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import sys
import gzip
import re

codon_tot = {}
starts = []
rev_ends = []
joins = []
rev_joins = []

'''
For matching the expected output, must include the 'joins'
However, joins are not complete genes, and shouldn't be included.
Joined sections are commented out (comment in for full answer)

CDS only answers given here:
ATG 3871
GTG 338
TTG 80
ATT 4
CTG 2
'''

def reverse(dna):
	ntp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	rdna = ''
	
	for i in range(len(dna)):
		rdna += ntp[dna[len(dna)- 1 - i]]
	return rdna

with gzip.open(sys.argv[1], 'rt') as fp:
	cdsline= 'CDS\s+(\d+)\.\.(\d+)'	
	rev_cdsline = 'CDS\s+complement\((\d+)\.\.(\d+)\)'
	
'''
	joincdsline= 'CDS\s+join\((\d+)\.\.\d+\W\d+\.\.\d+\)'	
	joincdslongline = 'CDS\s+join\((\d+)\.\.\d+\W\d+\.\.\d+\W\d+\.\.\d+\)'
	join_rev_cdsline = 'CDS\s+complement\(join\((\d+)\.\.\d+\W\d+\.\.\d+\)\)'
'''

	for line in fp.readlines():
		match = re.search(rev_cdsline, line)
		if match:
			rev_ends.append(match.group(2))
		match = re.search(cdsline, line)
		if match:
			starts.append(match.group(1))
'''
		match = re.search(joincdsline, line)
		if match:
			joins.append(match.group(1))
		match = re.search(join_rev_cdsline, line)
		if match:
			rev_joins.append(match.group(1))
		match = re.search(joincdslongline, line)
		if match:
			joins.append(match.group(1))
'''
			
with gzip.open(sys.argv[1], 'rt') as fp:	
	dna = ''
	temp = 0
	for line in fp.readlines():
		dnaline = '\s+\d+\s+(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)'
		match = re.search(dnaline, line)
		if match: 
			for i in range(6):
				dna += match.group(i + 1)
	
for start in starts:
	codon = dna[int(start) - 1:int(start) + 2].upper()
	if codon in codon_tot:
		codon_tot[codon] += 1
	else:
		codon_tot[codon] = 1

rdna = reverse(dna.upper())

for end in rev_ends:	
	idx = len(rdna) - int(end)
	codon = rdna[idx:idx + 3].upper()
	if codon in codon_tot:
		codon_tot[codon] += 1
	else:
		codon_tot[codon] = 1
'''
for start in joins:
	codon = dna[int(start) - 1:int(start) + 2].upper()
	if codon in codon_tot:
		codon_tot[codon] += 1
	else:
		codon_tot[codon] = 1
	
for end in rev_joins:	
	idx = len(rdna) - int(end)
	codon = rdna[idx:idx + 3].upper()
	if codon in codon_tot:
		codon_tot[codon] += 1
	else:
		codon_tot[codon] = 1
'''

sorted(codon_tot.items(), key=lambda x:x[1])
for k, y in codon_tot.items():
	print(k, y)

print(sum(codon_tot.values()))

		 
"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
