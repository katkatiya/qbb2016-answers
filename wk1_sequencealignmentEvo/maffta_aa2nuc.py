#!/usr/bin/env python

from sys import argv
"""
translate aligned amino acids from MAFFT output back to nucleic acids.
if theres a - for a codon add three - (---)

"""


script, filename = argv
header = ''
sequence = ''

# def translate_dna(sequence):
aa_to_codon = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}
codon_to_aa= {y:x for x,y in aa_to_codon.iteritems()}
codon_to_aa['-'] = '---'
codon_to_aa["X"] = 'xxx' #I don't know what transeq X means. stop codon? could be a couple things


header = ''
sequence = ''

for line in open(filename):
    line = line.rstrip("\r\n")
    if line[0] == ">":
        header = line
        print header
    else:
        # line = line.rstrip("\r\n")
        #find and print nucleic acids that correspond to codons
        for i in range(0,len(line)):
            codon = line[i]
            sequence += codon_to_aa[codon]
    if sequence != '':
        print sequence
    sequence = ''
    




#save as fasta.fa in command window


