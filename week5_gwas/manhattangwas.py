#!/usr/bin/env python

from __future__ import division
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



"""
make a manhattan plot
y= log10(pval)
x= chromosome position
"""
for f in sys.argv[1:]:
    df = pd.read_table(f, delim_whitespace=True)
    dnom = df['P']
    
    pval_log = -1*(np.log10(dnom))
    #print pval_log
    title = f
    figtitle = "{}.png".format(title)

    plt.figure()
    plt.plot(pval_log, 'o')
    plt.title(title)
    plt.savefig(figtitle)
    plt.close()
    #plt.show()