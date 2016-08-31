#!/usr/bin/env python

"""Parse a single fasta record from stdin and print it"""

import sys

#what if want to parse just the first record?

line = sys.stdin.readline()
# verify isheader line
assert line.startswith( ">" )

#indentifer = line[1:].rstrip( "\r\n" ) # extract id --whole line
indentifer = line[1:].split()[0]
#print indentifer

seq = [] #create list of sequences

while 1:
    line = sys.stdin.readline().rstrip("\r\n")
    if line == "" or line.startswith(">"):
        break
    else:
        seq.append(line)
        
        
print indentifer, "".join(seq)