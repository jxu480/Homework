# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import mcb185
import sys

def kmer(seq, ksize):
	pairs = {'AA': 0, 'AC': 0, 'AG': 0, 'AT': 0, 'CA': 0, 'CC': 0, 'CG': 0, 'CT': 0, 
			'GA': 0, 'GC': 0, 'GG': 0, 'GT': 0, 'TA': 0, 'TC': 0, 'TG': 0, 'TT': 0}
	for i in range(len(seq) - ksize + 1):
		sec = seq[i:i+ksize]
		pairs[sec] += 1
	
	return pairs
	



for name, seq in mcb185.read_fasta(sys.argv[1]):
	ksize = int(sys.argv[2])
	total = kmer(seq, ksize)

	for i in total:
		print(i, total[i])

"""
python3 61kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
