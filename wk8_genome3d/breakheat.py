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

ennnnnrichments = (counts/e)
ennnnnrichments = np.log10(ennnnnrichments +1)


print control


