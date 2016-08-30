#!/usr/bin/env python

import sys

#sam = "~/qbb2016-answers/day1-hmwk/hiresults.sam"
#path2 = "~/qbb2016-answers/day2-morning/"
t_align = 0
t_align_match = 0
t_1loc =0
count = 0
summapQ = 0

for line in sys.stdin: #sam:
    if line.startswith( "@" ): #cheap way to do this
        #print line.rstrip("\r\n")
        continue
    else:
        #t_align = t_align + 1 #count all the alignments #problem 1 count total alignments
   
        fields = line.rstrip( "\r\n" ).split("\t")
        #if fields[5].find( "M") != -1:
            #t_align_match = t_align_match +1 #problem 2
            #print "found match"
            #if line.find("HO:i") != -1: #problem 3
                #t_1loc = t_1loc +1
            #print fields[2] #problem 4 print the chromosome if rna-seq matches for first 10 alignments
        count = count +1 #problem 4,5
        summapQ = summapQ + int( fields[4]) #problem 5
        #print summapQ #for debugging purposes only
        #if count >= 10: #problem 4
            #break #problem 4

    
print " "
print (summapQ/count) #"done" #t_1loc #t_align, t_align_match
