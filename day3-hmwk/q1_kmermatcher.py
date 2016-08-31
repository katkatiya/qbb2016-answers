#!/usr/bin/env python 


"""
Implement a script that finds matching kmers between a single query sequence 
and a database of targets. 


kmer_matcher.py <subset4400.fa> <query.fa> <k>


output (text file?--> nope pipe to head then >> )
target_sequence_name   target_start    query_start kmer

"""

import sys, fasta

#k = int(sys.argv[3]) #command line argument to change k
k=11
kmer_loc ={} #initilize kmer dictionary per sequence


for (ident,sequence) in fasta.FASTReader( open(sys.argv[1]) ): 
    sequence = sequence.upper()
    for i in range( 0, len(sequence) -k ):
        kmer = sequence[ i : i+k ]
        if kmer not in kmer_loc:
            kmer_loc[ kmer ] = [(ident,i)] 
        else:
            kmer_loc[kmer].append((ident,i))
#for kmer, loci in kmer_loc.iteritems():
    #print ident,kmer,loci #pipe this through less -S in command window. 


#now load query.fa compare to dictionary
for (ukn,query) in fasta.FASTReader( open(sys.argv[2]) ): 
    query = query.upper()
    for i in range( 0, len( sequence ) -k ):
        kmer_q = sequence[ i : i+k ]
        if kmer_q in kmer_loc:
            for ident, pos in kmer_loc[kmer_q]:
                print ident, pos, i, kmer_q
