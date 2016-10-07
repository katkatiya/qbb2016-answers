#!/usr/bin/env python

from __future__ import division
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


"""
make a histogram of allele frequency.

c(hom A1)/[c(hom A1)+c(hom A2)] 
"""

df = pd.read_table(sys.argv[1], sep='\t')

dnom = np.array(df)

freq = (dnom[:,4]) / (dnom[:,4] + dnom[:,6])
print freq

plt.figure()                       # Open blank canvas
#plt.title("FPKM") # Add a title to the top
plt.hist(freq)#,                    # ... plot a histogram of
        # bins=int(sys.argv[2]),                   # ... ... Use thirty bars
        # range=[minimum,maximum],   # ... ... ranging from the minimum to the maximum
        # normed=True,               # ... ... Normalize the bars to frequencies instead of counts
        # )

plt.ylabel("Frequency")            # Label the y-axis
# plt.show()

plt.savefig("hist_gwas.png")      # Save figure as .png
plt.close()