#!/usr/bin/env python


import sys
import re

"""
compute the number of contigs, 
minimum/maximum/average contig length, and N50. (Remember, you already have a FASTA parser from Bootcamp).

usage:

<contig_reader.py>  <conting.fa>

"""

contig_dir =open(sys.argv[1])
d={} #contig id and seq dictionary

#Jackies method for parsing fasta files with re.
records = re.findall(">.*\n[ATCGatcg\-\n]*",contig_dir.read(),re.M)
for fasta in records:
	id_sq = re.sub("[>\n]","",re.findall(">.*\n",fasta,re.M)[0])
	d[id_sq] = re.sub("[\n]","",re.sub(">.*\n","",fasta))
# print d #now we have a dictionary of IDs and sequences


sum_len=0
contig_len=[]
k=0

for i,contigs in enumerate(d):
    if i == 0:
        max_contig = len(d[contigs])
        min_contig = len(d[contigs])
        
    else:
        if len(d[contigs]) > max_contig:
            max_contig = len(d[contigs])
        if len(d[contigs]) < min_contig:
            min_contig = len(d[contigs])
            
    contig_len.append(len(d[contigs]))
    sum_len = sum_len+len(d[contigs])
    k = k+1
    
temp_sum = 0

#find N50
for contig in sorted(contig_len):
    temp_sum = temp_sum + contig
    if temp_sum > sum_len / 2:
        n50 = contig
        break
average_contig = sum_len/k

#write metrics to file
header = str(contig_dir)
metrics = ('{} min: {} max: {} average: {} n50: {}{}'.format('\n',min_contig,max_contig,average_contig,n50,'\n'))
# print header
# print metrics
with open('metrics', 'a+') as f:
    f.write(header)
    f.write(metrics)
    f.close()