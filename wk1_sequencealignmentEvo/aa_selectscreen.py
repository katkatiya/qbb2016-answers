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


line plot y= ratio(dS/dN) by x= codon position.
will tell you how conserved a domain is across homologs. 
i.e. larger response in y == more highly conserved.


usage: <./aa_selectscreen.py>  <week1_query.fa>  <nuc_alignedhomologs.fa>
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

score, score_all, dS, dN, dS_all, dN_all = [],[], [],[], [],[]
hcodon, qcodon = [], []
k=0 #nuc to codon counter

#compare all homologs to query
for line_h in homloggy:
    line_h = line_h.rstrip("\r\n")
    if line_h[0] == ">":

        if dN != []:
            #skip first loop because nothing to append yet
            if dN_all == []: 
                dS_all = [dS]
                dN_all = [dN]
            else:
                dS_all.append(dS)
                dN_all.append(dN)

            score, dS, dN = [],[],[]
        #print line_h
        continue
        
    elif line_h == "":
        continue
        
    else:
        if line_h[0] == ">":
            continue
        
        #cycle through query for each homolog
        for h,q in itertools.izip(line_h,itertools.cycle(qseq)):
            #now to add dS or dN for each homolog. compare codons
            k += 1
            hcodon.append(h)
            qcodon.append(q)
            if k == 3:
                hcodon = "".join(hcodon)
                qcodon = "".join(qcodon)
                if hcodon == qcodon:
                    #No change append a zero to both lists
                    dS.append(0)
                    dN.append(0)
                    #print "same"
                    flag = 1
                if hcodon == 'xxx':
                    #cannot count it
                    dS.append(0)
                    dN.append(0)
                    #print "xxx"
                    flag = 1
                if hcodon == '---':
                    dS.append(0)
                    dN.append(0)
                    #print "---"
                    flag = 1
                if flag ==0 and aa_to_codon[hcodon] == aa_to_codon[qcodon]:
                    dS.append(1)
                    dN.append(0)
                    #print aa_to_codon[hcodon] , aa_to_codon[qcodon]
                elif flag ==0 and aa_to_codon[hcodon] != aa_to_codon[qcodon]:
                    dS.append(0)
                    dN.append(1)
                    #print aa_to_codon[hcodon] , aa_to_codon[qcodon] #none of this?
                
                #reset for next comparison
                flag=0
                k=0
                hcodon = []
                qcodon = []


 
# score_all[0].pop(-1)
dS = np.array(dS_all)
dN = np.array(dN_all)
# print dS.shape, dN.shape
# quit()


dS_sum = np.sum(dS, axis=0)+1
dN_sum = np.sum(dN, axis=0)+1

N = np.log10(dN_sum)
S = np.log10(dS_sum)
# N = dN_sum
# S = dS_sum
ratio = S - N #ratio of N/S non sycn to sycn selections.
#print ratio

plt.style.use('ggplot')
plt.figure()
plt.plot(ratio)
plt.title("Functional conservation of gene sequence across homologs ")
plt.ylabel("Ratio dS/dN (log(dS)-log(dN))")
plt.xlabel("Amino acid position")
#plt.show()

plt.savefig("Functional conservation of gene sequence across homologs.png")
plt.close()



        
        
        
        
        
