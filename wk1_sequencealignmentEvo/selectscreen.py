#!/usr/bin/env python


from __future__ import division
import sys
import itertools
import numpy as np

"""
so now we should have all the blast hits that match our query. 
We converted nucleic acids to amino acids with transeq --> interested in functional changes
quickly align multiple sequences (by amino acid) by fft. 
convert back to nucleic to compare homologs to query fasta.


line plot y= ratio(dN/dS) by x= codon position.
will tell you how conserved a domain is across homologs. 


usage: selectionscreen.py <query.fa> <aligned_converted_homologs.fa>
"""

query = open(sys.argv[1])
homo = open(sys.argv[2])


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

k = 0 

#parse through query sequence
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
            
last_id =''
count =0
score_all =[]
for row in homo:
    if row.startswith( ">" ):
        indentifer = row[1:].split()[0]
        count +=1 #counting number of homologs
        print indentifer, count
    else:
        indentifer = last_id
        hseq = [] #create list of sequences
        for row2 in homo:
            row2 = row2.rstrip("\r\n")
            if row2.startswith(">"):
                last_id = row2[1:].split()[0]
                break
            elif row2 == "":
                continue
            else:
                hseq.append(row2)
        hseq = "".join(hseq)
        
        print len(hseq)
        # quit()
        
        hcodon = []
        qcodon = []
        ds_temp = 0
        dn_temp = 0
        score =[]
        #Have all of X homolog sequence no spaces. now compare to query
        for h,q in itertools.izip(hseq,qseq):
            #now to add dS or dN for each homolog. compare codons
            k +=1
            hcodon.append(h)
            qcodon.append(q)
            if k == 3:
                hcodon = "".join(hcodon)
                qcodon = "".join(qcodon)
                if hcodon == '---':
                    # print hcodon, qcodon , h, q
                    k=0
                    #if no spaces first homolog would align perfectly... 
                    #Mafft tried to align all the homologs to each other not to query... thaaaats why.
                    #ok well lets convert query to codons too and see if can get mult aligned to query. 
                    hcodon = []
                    qcodon = []
                    continue
                if aa_to_codon[hcodon] == aa_to_codon[qcodon]:
                    ds_temp +=1
                    score.append(1)
                    #print aa_to_codon[hcodon] , aa_to_codon[qcodon], ds_temp, dn_temp, h, q
                else:
                    dn_temp +=1 
                    score.append(-1)
                    #print aa_to_codon[hcodon] , aa_to_codon[qcodon], ds_temp, dn_temp, h, q
                #reset for next comparison
                k=0
                hcodon = []
                qcodon = []
        print len(score)
        if score_all == []:
            score_all = score
        else:
            score_all = np.vstack([score_all,score])
#print score_all
#print np.shape(score_all)
                

        
        
        
        
        
