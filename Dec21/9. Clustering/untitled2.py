from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

milk = pd.read_csv("D:\C-DAC\Datasets\milk.csv", index_col=0)
print(milk.shape)

scaler=StandardScaler()
milkscaled=scaler.fit_transform(milk)

pca=PCA()
prin_comp=pca.fit_transform(milkscaled)
print(milk.shape)
print(prin_comp)

pd_PC=pd.DataFrame(prin_comp,columns=['pc1','pc2','pc3','pc4','pc5'])
pd_PC.var()

print(pca.explained_variance_)
print(pca.explained_variance_*100)

from pca import pca
model=pca()
results=model.fit_transform(milkscaled)

plt.show(model.biplot(label=True,legend=False))