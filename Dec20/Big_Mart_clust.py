
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

train = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Cases\Big Mart Sales\processed_train.csv")


items_data=train[['Item_Type','i_weight','Item_Visibility',
                  'Item_MRP','Item_Outlet_Sales']]

items_means=items_data.groupby('Item_Type').mean()

##Dendogram

scaler = StandardScaler()
iscaled = scaler.fit_transform(items_means)

mergings = linkage(iscaled, method = 'average')

dendrogram(mergings, labels = list(items_means.index),
           leaf_rotation= 90,
           leaf_font_size = 10)
plt.show()

## K-Mean
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(iscaled)
    labels=km.predict(iscaled)
    sil.append(silhouette_score(iscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)
