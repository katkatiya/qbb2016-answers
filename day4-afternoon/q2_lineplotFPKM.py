#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
-creates a separate FPKM image for 2L 2R 3L 3R 4 and X
-has a title stating what chromosome is displayed using what window size. e.g. "Rolling mean (size = 200) for 3R"

-can be invoked from the command line as 

./plotFPKMbyPosition.py  <window_size>  <sample_1>   [ <sample_2> ...] 

"""
sample = len(sys.argv[0:])

for i in range (2,sample):
    df1 = pd.read_table( sys.argv[i] )
    srr = sys.argv[i].split('/')[-2]

    #filter for gene_name and FPKM > 0 
    chrList = ["2L","2R","3L","3R","4","X"]
    
    for j in chrList: 
        chX= df1["chr"] == j
        chX = df1[chX]    
        #print (chX)
        
        #binning FKPM (expr. values) window size = 200 transcripts
        smoothed = chX["FPKM"].rolling(int(sys.argv[1])).mean() #series object
        
        plt.figure()
        plt.plot(smoothed)
        plt.title("Rolling mean (size={}) for Chromosome {}".format(sys.argv[1],j))
        plt.xlabel(" Relative position of chromosome (line number)")
        plt.savefig("Rolling mean (size={}) for Chromosome {}.png".format(sys.argv[1],j))
        plt.close()
        






