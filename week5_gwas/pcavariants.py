#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



"""
make a pca plot of first two principle components variants across yeast samples.

"""

df = pd.read_table(sys.argv[1], sep=' ')

dnom = np.array(df)

x= dnom[:,2]
y= dnom[:,3]


plt.plot(x,y, "o")
plt.title("PCA of variants")
plt.xlabel("Principle component 1")
plt.ylabel("Principle component 2")
plt.savefig("pca_first2components.png")
# exit()