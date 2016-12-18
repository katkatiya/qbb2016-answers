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
positions_5c = file['0.positions'][...]
regions = file['regions'][...]


ennnnnrichments = (counts/e)
ennnnnrichments = np.log10(ennnnnrichments +1)

dict_ctcf = {}




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
ctcf_infrag = []
ctcf_pos = []

for p, startstop in enumerate(positions_5c):
    for element in dict_ctcf:
        # print startstop
        if int(element) > startstop[0] and int(element) < startstop[1]:
            #print startstop , element , p, positions_5c.shape
            ctcf_infrag.append(p)
            ctcf_pos.append(int(element))
    
# print ctcf_infrag
# print ctcf_pos

#print ennnnnrichments.shape

yayctcf = ennnnnrichments[ctcf_infrag,:][:,ctcf_infrag]
yayctcf[np.isnan(yayctcf)] = -np.inf

test = np.amax(yayctcf, axis=0)
test2= np.argmax(yayctcf, axis=0)

print yayctcf #print to txt file
#print test
#print test2

#need to skip over nan values 
 


            
            
        
            



