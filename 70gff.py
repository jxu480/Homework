# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json
import sys
import re
import gzip

with gzip.open(sys.argv[1], 'rt') as fp:
	infoline = '\w+\.\w+\s+\w+\s+gene\s+(\d+)\s+(\d+)\s+\.\s+(\S)\s+\.\s+\S+;\S+;Name=(\w+)'
	nameline = 'Name=(\S+);'
	gene_info = []
	for line in fp.readlines():
		match = re.search(infoline, line)
		if match:
			begin = match.group(1)
			end = match.group(2)
			sense = match.group(3)
			name = match.group(4)
			
			gene = {'gene':name, 'beg':begin, 'end':end, 'strand':sense}
			gene_info.append(gene)
			
print(json.dumps(gene_info, indent = 4))

"""	
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
