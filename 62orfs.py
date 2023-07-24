# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import mcb185
import sys
import argparse

def findorf(seq, num = 0):	
	start_end = {}
	first = False
	for i in range(len(seq)):
		if seq[i] == 'M' and first == False:
			startidx = i * 3 + 1 + num
			first = True
		if seq[i] == '*' and first == True:
			endidx = (i + 1) * 3 + num
			start_end[startidx] = endidx
			first = False
	return start_end
	
def reverse(dna):
	ntp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	rdna = ''
	
	for i in range(len(dna)):
		rdna += ntp[dna[len(dna)- 1 - i]]
	return rdna


for name, seq in mcb185.read_fasta(sys.argv[1]):
	name = name.split()
	
	for i in range(3):
		aaseq = mcb185.translate(seq[i:])
		orfs = findorf(aaseq, i)
		for key, value in orfs.items():
			if value - key > 300:
				startidx = int((key - i - 1)/3)
				print(name[0], key, value, '+', aaseq[startidx:startidx + 10])

for name, seq in mcb185.read_fasta(sys.argv[1]):
	name = name.split()

	for i in range(3):	
		rev_aaseq = mcb185.translate(reverse(seq)[i:])
		rev_orfs = findorf(rev_aaseq, i)
		for key, value in rev_orfs.items():
			if value - key > 300:
				startidx = int((key - i - 1)/3)
				print(name[0], len(seq)- value + 1, len(seq) - key + 1, '-', 
				#reading from the same way as the + strand
				rev_aaseq[startidx:startidx + 10])


"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz | sort -nk 2
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
