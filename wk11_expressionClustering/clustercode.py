#!/usr/bin/env python


import scipy.cluster.hierarchy as hc
import sys
import pandas as pd
from matplotlib import pyplot
import numpy as np
import scipy


"""
load gene expression dataset generate heatmaps 
from various clustering methods. all rows are genes,
each column corresponds to one cells type

useage: ./clustercode.py hema_data.txt

"""

#load dataset
d = pd.read_csv(open(sys.argv[1]), sep = " ", delimiter="\t", index_col = 0)

#make arrays
data = np.array(d)
celltype = data.T
colum = d.columns

# heatmap = pyplot.pcolor(data)
# pyplot.show()

#Plot: Clustered heatmap of gene expression.
link_gene = hc.linkage(data, method='centroid')
linkorder = hc.leaves_list(link_gene)

link_celltype = hc.linkage(celltype, method='centroid')
cellorder = hc. leaves_list(link_celltype)

data2 = data[linkorder,:]
data3 = data2[:, cellorder]
heatmap = pyplot.pcolor(data3)
pyplot.title("Hierachal clustering gene expression per cell type")

pyplot.savefig('sortedheatmap.png')

#Plot: k-means clustering of genes plotted against CFU and poly.
#kmeans = scipy.kmeans2()


#Plot: Dendrogram of cell types
fig = pyplot.figure(figsize=(8,8))
dendo = hc.dendrogram(link_celltype, orientation='top', labels=colum)
pyplot.title("Dendrogram of cell types")
pyplot.savefig("cell type dendogram")



#Text: List of differentially expressed genes.


#Text: Panther output, known function of gene, comment on possible role in differentiation.
