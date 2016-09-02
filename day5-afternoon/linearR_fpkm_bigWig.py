#!/usr/bin/env python

import sys 
import pandas as pd
import numpy as np

from statsmodels.regression.linear_model import OLS as ols

"""
BIG WIG COLUMNS
   name - name field from bed, which should be unique
   size - size of bed (sum of exon sizes
   covered - # bases within exons covered by bigWig
   sum - sum of values over all bases covered
   mean0 - average over bases with non-covered bases counting as zeroes
   mean - average over just covered bases


usage:

linearR...py   <t_data.csv>                                 <bigWig.tab>
            ~/data/results/string/SRR*893/t_data.ctab     ~/qbb.../day5-afternoon/*tab
"""

df_fpkm = pd.read_csv( sys.argv[1], "\t") #may need read csv
df_histones = pd.read_csv( sys.argv[2], "\t", names=["name","window","covered","sum","mean0","mean"] )


chromesome_type=["X","3R","3L","2R","2L","4"]
result_df=[]
for item in chromesome_type:
	result_df.append(df_fpkm[df_fpkm["chr"] == item])

data_df= pd.concat(result_df).sort(["t_name"])

# print(data_df)
df_histones=df_histones.sort(["name"])
# print(len(df_histones["sum"]),len(data_df["FPKM"]))
# quit()


#fpkm is response, while average histone expresion is predictor
if len(df_histones["sum"])==len(data_df["FPKM"]):
	ols_md= ols(df_histones["sum"].tolist(),data_df["FPKM"].tolist())

results = ols_md.fit()
print(results.summary())




