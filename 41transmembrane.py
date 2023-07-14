# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

# KD: Kyte-Doolittle scale indicates hydrophobic amino acids

import sys
import gzip
import mcb185

# any 8 in the amino acids that have a average KD greater than 2.5 

def KD(aa):
	acid = 'ACDEFGHIKLMNPQRSTVWY'
	hydro = [1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, 
	-4.5, -0.8, -0.7, 4.2, -0.9, -1.3]

	return hydro[acid.index(aa)]

def hah(seq, winsiz, threshold):
	# hydrophobic alpha helix	
	for i in range(len(seq) - winsiz):
		window = seq[i:i + winsiz]
		kd = 0
		a = 0
		
		for aa in window:
			if aa == 'P':
				break
			kd += KD(aa)
			a += 1
				
		if a == winsiz and (kd/a) > threshold:
			return True		
	return False

total = 0

for name, seq in mcb185.read_fasta(sys.argv[1]):	
	if hah(seq[:30], 8, 2.5) and hah(seq[30:], 11, 2.0): 
		total += 1
		print(name)

print(total)		

"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
