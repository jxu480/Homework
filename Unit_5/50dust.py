# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import sys
import mcb185
import math

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

# setting default
winsiz = 10
threshold = 1.5

for i in range(len(sys.argv)):
	if sys.argv[i] == '-w':
		winsiz = int(sys.argv[i + 1])
	if sys.argv[i] == '-t':
		threshold = float(sys.argv[i + 1])
	if sys.argv[i] == '-s':
		fp = sys.argv[i + 1]

for name, seq in mcb185.read_fasta(fp):
	mask = list(seq.upper())
	
	for i in range(len(seq) - winsiz + 1):
		wind = seq[i:i+winsiz]
		if seqentr(wind) < threshold:
			for j in range(i, i + winsiz):
				mask[j] = mask[j].lower()
	m = ''.join(mask)
	
	print('>' + name)
	for i in range(0, len(m), 60):
		print(m[i:i + 60])

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
