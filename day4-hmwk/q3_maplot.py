#!/usr/bin/env python

import sys #re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Instead of plotting FPKM values for SRR072893 and SRR072915 directly, 
transform the data to make an MA-plot. This time do not drop rows with 0 FPKM. 
plt.scale( 'log' ) is not enough so you will have to log etc your values first.


usage:
./q2_hist.py <SRR072893 t_data.ctabt> <SRR072915 t_data.csv>

"""

df1 = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

# fpkm1 = df1["FPKM"]+1
logfpkm1 = np.log10(df1["FPKM"]+1).tolist()
logfpkm2 = np.log10(df2["FPKM"]+1).tolist()

#Reformat into ma plot
MA_data_M=[]
MA_data_A=[]
# print(FPKM1_data)

for i,out in enumerate(logfpkm1):
	MA_data_M.append(logfpkm1[i]-logfpkm2[i])
	MA_data_A.append(0.5*(logfpkm1[i]+logfpkm2[i])) 

# print(MA_data_Y)
# print(ctab_data[filter_FPKM])
plt.figure()
#plt.title("MA for {} in MA view".format(re.findall("SRR[0-9]*/",sys.argv[1]),re.findall("SRR[0-9]*/",sys.argv[2])))

plt.scatter(x=MA_data_A,y=MA_data_M, alpha=0.1)
# plt.show()
plt.savefig("SRR893_SRR915 MAplot .png")
plt.close()



