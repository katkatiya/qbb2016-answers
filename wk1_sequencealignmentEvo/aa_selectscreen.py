#!/usr/bin/env python



import sys
import itertools
import numpy as np
import matplotlib.pyplot as plt

"""
so now we should have all the blast hits that match our query. 
We converted nucleic acids to amino acids with transeq --> interested in functional changes
quickly align multiple sequences (by amino acid) by fft. 
convert back to nucleic to compare homologs to query fasta.


line plot y= ratio(dN/dS) by x= codon position.
will tell you how conserved a domain is across homologs. 


usage: selectionscreen.py <query_aminoacids.fa> <aligned_aminoacids.fa>
"""

query = open(sys.argv[1])
homloggy = open(sys.argv[2])


qseq= []
for i, line in enumerate(query):
    line = line.rstrip("\r\n")
    if line[0] == ">":
       pass
    elif line =="":
        continue
    else:
        qseq.append(line)
qseq = "".join(qseq)
#print len(qseq)

# codon diction from stack overflow:
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
'xxx':'X'
}

score, score_all, dS, dN, dS_all, dN_all= [],[], [],[], [],[]
#compare all homologs to query
for line_h in homloggy:
    line_h = line_h.rstrip("\r\n")
    if line_h[0] == ">":
        if score != []:
            #skip first loop because nothing to append yet
            if score_all == []: 
                score_all = [score]
                dS, dN = [dS],[dN]
            else:
                score = score[:-1]
                dS,dN = dS[:-1],dN[:-1]

                dS_all.append(dS)
                dN_all.append(dN)
                #score_all.append(score)

            score, dS, dN = [],[],[]
        #print line_h
        continue
    elif line_h == "":
        continue
    else:
        if line_h[0] == ">":
            continue
        print line_h
        quit()
        #cycle through query for each homolog
        for h,q in itertools.izip(line_h,itertools.cycle(qseq)):
            if h == q:
                score.append(1)
                dS.append(1)
                dN.append(0.1)
            else:
                score.append(-1)
                dS.append(0.1)
                dN.append(1)
            #print h,q, score

"""hmmm if there's no change in the (same codon, same sequence)
I shouldn't count that as a dS. Will change if I have time. onto graphing
"""


score_all[0].pop(-1)
dS = np.array(dS_all)
dN = np.array(dN_all)
dS_sum = np.sum(dS, axis=0)
dN_sum = np.sum(dS, axis=0)
#print dS_sum.shape, dN_sum.shape

ratio = dN_sum / dS_sum #ratio of N/S non sycn to sycn selections.



#print mean_scores

plt.figure()
plt.plot(ratio)
plt.title("many lines?")
plt.ylabel("Ratio dN/dS")
plt.xlabel("hopefully aa position")
plt.show()

# plt.savefig("Rolling mean (size={}) for Chromosome {}.png".format(sys.argv[1],j))
# plt.close()



        
        
        
        
        
