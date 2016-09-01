#!/usr/bin/env python

import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

"""
Create a density plot of the FPKM values for SRR072893.

usage:
./q2_hist.py <SRR072893 t_data.ctabt> 
"""


df1 = pd.read_table(sys.argv[1])
# fpkm1 = np.array(df1["FPKM"]).reshape(-1,1)
fpkm1 = df1["FPKM"].tolist()
density=gaussian_kde(fpkm1)


#script below from stack overflow *Ji
plt.figure()
plt.title("FPKM {} in Density view".format(re.findall('SRR[0-9]*',sys.argv[1])))
xs = np.linspace(0,10,100)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
# plt.show()
plt.savefig("task4density.png")
plt.close()