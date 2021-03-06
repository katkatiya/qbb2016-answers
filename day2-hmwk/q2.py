#!/usr/bin/env python

"""
Write a python script for identifier mapping. Use input mapping file (txt) and c_tab from stringTie
to identify corresponding translation from mapping file. 

If found, print line from c_tab with identifier
if not found, print nothing (ignore)
              print field with default value ('None')
"""

import sys


#Name those inputs
fmap = open(sys.argv[1]) #use map text generated in q1
ctab = open(sys.argv[2]) #t_data.ctab is the only file with FlyIDs
out = sys.argv[3] #equal 0 or 1 to change output to print ignore or print 'None'

fmap_dic={} #initialize dictionary

#build dictionary from fmap file
for line in fmap:
    field = line.rstrip('\r\n').split("\t")
    fmap_dic[  field[0] ] = field[1] 
    
    #for i in fmap_dic:
        #print i , fmap_dic[i]
        
j=0
if out == "0":
    for i, genes in enumerate(ctab): 
        flyd = genes.rstrip('\r\n').split("\t")[8]
        #print flyd #for debugging suppress    
        if j ==100:
            break
      
        if flyd in fmap_dic: #only print genes that map, ignore unmapped
            print flyd +'\t'+ fmap_dic[flyd]
            j+=1


j=0    
if out == "1":        
    for i, genes in enumerate(ctab): 
        flyd = genes.rstrip('\r\n').split("\t")[8]
        #print flyd #for debugging suppress    
        if j ==100:
            break
      
        if flyd not in fmap_dic:   
            print "not found"
            j+=1
        elif flyd in fmap_dic:
            print flyd +'\t'+ fmap_dic[flyd]
            j+=1
