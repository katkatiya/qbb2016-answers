#!/usr/bin/env python

import sys

"""
Filter and convert blast.tsv to a fasta file. input on command line to obtain blast homology from week1_query.fa is as follows:
"blastn -db nr -query week1_query.fa -evalue 0.0001 -outfmt "6 sseqid qstart qend sseq" -remote -out blastNR_wk1.tsv"

"""
f = open(sys.argv[1])
k=0
for i, line in enumerate(f):
    fields = line.rstrip( "\r\n" ).split("\t")
    idr = fields[0].split("|")
    # print idr[-1]
    if int(fields[1]) == 1 and int(fields[2])== 10293:
        k+=1
        print ">{}".format(idr[3])
        print fields[-1]
print k
#now run in command line and save to a .fa file. 
        
