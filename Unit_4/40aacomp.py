# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import gzip
import sys
'''
tup = 'A', 0.5, 0.5
tup1 = 'B', 0.3, 0.7

arr = [tup, tup1]

print(arr)
'''

with gzip.open(sys.argv[1],'rt') as fp:
	total = 0
	acids = [0] * 20
	aa = 'ACDEFGHIKLMNPQRSTVWY'
	
	arr = fp.readlines()
		
	for i in range(len(arr)):
		line = arr[i]	
		
		if line[0] == '>':
			continue			
		
		for acid in aa:
			for j in line:
				if j == acid:
					acids[aa.index(acid)] += 1
		
for i in range(len(aa)):	
	print(aa[i], acids[i], f'{acids[i]/sum(acids):.4f}')

"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
