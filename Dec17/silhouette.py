import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


milk = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\milk.csv",
                   index_col = 0)

scaler = StandardScaler()
milkscaled = scaler.fit_transform(milk)

#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(milkscaled)
    labels=km.predict(milkscaled)
    sil.append(silhouette_score(milkscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)


####Nutrient###

nutrient = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\nutrient.csv",
                   index_col = 0)

scaler = StandardScaler()
nutrientscaled = scaler.fit_transform(nutrient)

#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(nutrientscaled)
    labels=km.predict(nutrientscaled)
    sil.append(silhouette_score(nutrientscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

####Boston###
boston = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Boston.csv",
                   index_col = 0)

scaler = StandardScaler()
bostonscaled = scaler.fit_transform(boston)

#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(bostonscaled)
    labels=km.predict(bostonscaled)
    sil.append(silhouette_score(bostonscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)


km=KMeans(n_clusters=2,random_state=2022)
km.fit(bostonscaled)
labels=km.predict(bostonscaled)

boston['Cluster']=labels
boston.sort_values('Cluster',inplace=True)


#Calculating the centroids
boston.groupby('Cluster').mean()




