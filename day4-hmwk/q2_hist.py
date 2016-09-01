#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Create a histogram of the FPKM values for SRR072893.
-filter out zero-values
-log values

usage:
./q2_hist.py <t_data.csv> <hist bin?>

"""

df = pd.read_table(sys.argv[1])

#filter for FPKM > 0 
fpkmnotzero = df["FPKM"] > 0
fpkm_filt = df[fpkmnotzero]["FPKM"]
#plot the log() of found fpkm values
log_fpkm = np.log10(fpkm_filt)


#plot a histogram of your t_data here

plt.figure()                  # Open blank canvas
plt.hist(log_fpkm)            # Generate a histogram of the data, with defaul settings


plt.savefig("default_hist.png") # Save the figure
plt.close()                   # Close the canvas

minimum = np.min(log_fpkm)           # Grab the minimum...
maximum = np.max(log_fpkm)           # ...and maximum value to set the range

plt.figure()                       # Open blank canvas
plt.title("FPKM") # Add a title to the top
plt.hist(log_fpkm,                    # ... plot a histogram of
        bins=int(sys.argv[2]),                   # ... ... Use thirty bars
        range=[minimum,maximum],   # ... ... ranging from the minimum to the maximum
        normed=True,               # ... ... Normalize the bars to frequencies instead of counts
        )

plt.ylabel("Frequency")            # Label the y-axis
plt.savefig("clean_hist.png")      # Save figure as .png
plt.close()                       # Close the canvas
