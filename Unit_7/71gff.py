# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file

import sys
import gzip
import re
import json

def matching(match):
	name = match.group(5)
	begin = int(match.group(2))
	end = int(match.group(3))			
	sense = match.group(4)
	gene = {'gene':name, 'beg':begin, 'end':end, 'strand':sense}
	return gene

with open(sys.argv[1]) as fp:
	gene_line = '(\w+)\s+WormBase\s+gene\s+(\d+)\s+(\d+)\s+\.\s+(\S)\s+\.\s+\S+;\S+;\S+;sequence_name=(\S+);\S+;\S+;\S+;'
	alt_gene_line = '(\w+)\s+WormBase\s+gene\s+(\d+)\s+(\d+)\s+\.\s+(\S)\s+\.\s+\S+;\S+;sequence_name=(\S+);\S+;\S+;\S+;'
	gene_info = {}
	for line in fp.readlines():	
		match = re.search(gene_line, line)
		if match:
			if match.group(1) not in gene_info.keys():
				gene_info[match.group(1)] = []
			gene = matching(match)
			gene_info[match.group(1)].append(gene)	
		
		else:		
			match = re.search(alt_gene_line, line)
			if match:
				if match.group(1) not in gene_info.keys():
					gene_info[match.group(1)] = []
				gene = matching(match)
				gene_info[match.group(1)].append(gene)	
	
	print(json.dumps(gene_info, indent = 4))
	
	total = 0
	for key in gene_info:
		total += len(gene_info[key])
		print(key, len(gene_info[key]))
	print(total)

"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
