#!/usr/bin/env python

import h5py
import sys
import numpy as np


control = open(sys.argv[1]) #ctcf_peaks

file = h5py.File("fragments.heat")
file.keys()
[u'0.counts', u'0.expected', u'0.positions', u'regions']
counts = file['0.counts'][...]
e = file['0.expected'][...]
positions = file['0.positions'][...]
regions = file['regions'][...]


ennnnnrichments = (counts/e)
ennnnnrichments = np.log10(ennnnnrichments +1)

dict_ctcf = {}


# print regions
# quit()


# need to run through ctcf file and compare positions to 5C
for i, line in enumerate(control):
    ctcf = line.rstrip( "\r\n" ).split('\t')
    if line.startswith('#Chromosome'):
        continue
    if ctcf[0] == 'chrX':
         dict_ctcf[ctcf[1]] = ctcf[1]
        # print ctcf_pos
        # quit()

#now I want to compare to positions of the enrichments. 


for p, startstop in enumerate(positions):
    for element in dict_ctcf:
        # print startstop
        if element > startstop[0]:
            if element < startstop[1]:
                print positions
            



