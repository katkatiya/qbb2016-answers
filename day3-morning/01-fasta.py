#!/usr/bin/env python

"""Parse a single fasta record from stdin and print it"""

import sys

class FASTReader(object):
    def __init__( self, file ):
        self.file = file
        self.last_id = None

    def next(self):
        if self.last_id is None:
            line = self.file.readline()
            # verify isheader line
            assert line.startswith( ">" )
            #indentifer = line[1:].rstrip( "\r\n" ) # extract id --whole line
            indentifer = line[1:].split()[0]
        else:
            indentifer = self.last_id

        seq = [] #create list of sequences

        while True:
            line = sys.stdin.readline().rstrip("\r\n")
            if line.startswith(">"):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                return None, None
            else:
                seq.append(line)
                
        return indentifer, "".join(seq) 


#What I actually want
reader = FASTReader(sys.stdin)

while 1:
    indentifer, seq = reader.next()
    if indentifer is None:
        break
    print indentifer, seq