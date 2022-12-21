import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN

milk = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\milk.csv",
                   index_col = 0)

scaler = StandardScaler()
milkscaled=scaler.fit_transform(milk)


#clust_DB = DBSCAN(eps=0.4, min_samples=3)
#clust_DB.fit(milkscaled)
#print(clust_DB.labels_)

eps_range = [0.1,0.2,0.3,0.4,0.6,1]
mp_range = [2,3,4,5]
cnt = 0
a = []

for i in eps_range:
    for j in mp_range:
        clust_DB = DBSCAN(eps = i, min_samples = j)
        clust_DB.fit(milkscaled)
        if len(set(clust_DB.labels_)) >= 2:
            cnt = cnt + 1
            sil_sc = silhouette_score(milkscaled,clust_DB.labels_)
            a.append([cnt,i,j,sil_sc])
            print(i,j,sil_sc)
            
a = np.array(a)
pa = pd.DataFrame(a,columns=['Sr','eps','min_pt','sil'])
print("Best Paramters:")
#max_score = pa['sil'].max()
pa[pa['sil'] == pa['sil'].max()]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
 