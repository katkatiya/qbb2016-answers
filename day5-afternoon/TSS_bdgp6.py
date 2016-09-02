#!/usr/bin/env python

import sys 
import pandas as pd
import numpy as np

"""
Create a dictionary 

TSS_bdgp6.py    < ~/data/results/string/SRR*893/t_data.ctab>

"""

df = pd.read_table( sys.argv[1])
n, p = df.shape


#filter for chromosome
chrList = ["2L","2R","3L","3R","4","X"]

for i,row in df.iterrows():
    if row[1] in chrList: 
        if row[2] is "+" :
            start=(row[3] -500)
            end=(row[3]+ 500)

        else:
            start=(row[4]-500)
            end=(row[4]+500)

        #Want a .bed file with Chromosome start#(-500) end#(+500) t_name
        print "{}\t{}\t{}\t{}".format(row[1], start, end, row[5])


# bedarray = np.insert([start][2],[end][2])
# print bedarray
