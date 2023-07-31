# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import mcb185
import gzip
import math

altseq = ''

winsiz = int(sys.argv[2])
threshold = float(sys.argv[3])

'''
#returns probability of nucleotide
def prob(nt, seq):
	a = 0
	c = 0
	t = 0
	g = 0
	
	for n in seq:
		if n == 'A':
			a += 1
		if n == 'C':
			c += 1
		if n == 'T':
			t += 1
		else:
			g += 1
	
	if nt == 'A':
		return (a/len(seq))
	if nt == 'C':
		return (c/len(seq))
	if nt == 'T':
		return (t/len(seq))
	if nt == 'G':
		return (g/len(seq))	

#return the shannon entropy of one section
def shanentr(seq):
	total = 0
	for nt in seq:
		total += prob(nt, seq) * math.log(prob(nt, seq), 2)
	
	return total * -1
'''		

def entropy(P):
	assert(math.isclose(sum(P), 1))
	h = 0
	for p in P:
		h -= p * math.log2(p)
	
	return h
	
def seqentr(seq):
	a = seq.count('A') / len(seq)
	c = seq.count('C') / len(seq)
	g = seq.count('G') / len(seq)
	t = seq.count('T') / len(seq)
	
	p = []
	if a != 0: p.append(a)
	if c != 0: p.append(c)
	if g != 0: p.append(g)
	if t != 0: p.append(t)
	
	return entropy(p)
			
# run each sequence through the shanentr function
# compare the outcome to the threshold
# replace everything in that with 'N'

print(seqentr('AACCGGT'))

for name, seq in mcb185.read_fasta(sys.argv[1]):
	mask = list(seq)
	
	for i in range(len(seq) - winsiz + 1):
		wind = seq[i:i+winsiz]
		if seqentr(wind) < threshold:
			for j in range(i, i + winsiz):
				mask[j] = 'N'
	m = ''.join(mask)
	
	for i in range(0, len(m), 60):
		print(m[i:i + 60])


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNNNNNNNNNNNGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNNNNNNNNNNNTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNNNNNNNNNNNCTTAGG
TCACNNNNNNNNNNNNCCAATATAGGCATAGCGCACAGNNNNNNNNNNNNNNNNGAGTNN
NNNNNNNNNNTGAAACGCATTAGCACCACCATNNNNNNNNNNNNNNNNNTTACCACAGGT
AACNNNNNNNNNNNACGCGTACAGNNNNNNNNNNNNNNNNNNCGCACCTGACAGTGCNNN
NNNNNNNNNNNNNCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNNNNNNNNNNNNNNCCANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGTG
GCGATNNNNNNNNNNNNNNNNNGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
