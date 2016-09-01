#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Create a boxplot for all the Sxl transcripts that have an FPKM >0 in SRR072893 and SRR072915. 
log() the values, add a title, label the y-axis, and label each sample on the x-axis.

"""
numarg = len(sys.argv[1:])


for i in range (1,numarg+1):

    df1 = pd.read_table( sys.argv[i] )
    srr = sys.argv[i].split('/')[-2]#.find("SRR")

    #filter for Sxl gene_name and FPKM > 0 
    sxl_temp = df1["gene_name"] == "Sxl"
    sxl = df1[sxl_temp]

    sxl_ex_temp = sxl["FPKM"] > 0
    sxl_ex = sxl[sxl_ex_temp]
    #print sxl_ex

    #plot the log() of found fpkm values
    fpkm = sxl_ex["FPKM"]
    log_fpkm = np.log10(fpkm) #natural log is default use log10
    
    if i == 1:
        srr_all = [srr]
        logfpkm_all = [log_fpkm]
    else:
        srr_all.append(srr)
        logfpkm_all.append(log_fpkm) 



#end loop BEGIN PLOT

plt.figure()                       # Open a blank canvas
plt.boxplot(logfpkm_all,labels=srr_all)

plt.xticks(rotation=90)
plt.ylabel("Log10 FPKM")              # Label the y-axis
plt.xlabel("Samples cross Dros. development")              # Label the x-axis 
plt.title("Sxl Transcript Expression level (FPKM)") # Add a title to the top
plt.subplots_adjust(bottom = 0.25)   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
plt.savefig("clean_boxplot.png")   # Save the plot
plt.close()                        # Close the canvas




