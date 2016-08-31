#!/usr/bin/env python

"""
Parse http://www.uniprot.org/docs/fly.txt and output a new file 
with two tab separated columns, col 1 = FlyBase ID (flybase gene ac), col 2= Uniprot ID (AC)
"""

import sys

#download fly.txt and put in a working directory
fly = "/Users/cmdb/qbb2016-answers/day2-hmwk/flybase.txt" #hardcode filepath for document of interest
f= open(fly) # hardcoded not typically recommended, but only using this file.
f2 = open('flygene_uniprot_mapper.output','w') #open new .txt to save to

for lines in f: #.readline:
    if lines.find( "DROME" ) != -1: #find DROME
        fields = lines.rstrip("\r\n").split()
        if "DROME" in fields[0]: #ignore empty fields
            continue
        else:
            #print fields[3],fields[2]  #(suppressed) output to the command line 
            f2.write("%s\t%s\n" % (fields[3],fields[2])) #write to txt file
        

            
            