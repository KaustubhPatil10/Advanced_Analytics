#from scipy.cluster.hierarchy import linkage, dendrogram 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

milk = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\milk.csv",
                   index_col = 0)

scaler = StandardScaler()
milkscaled = scaler.fit_transform(milk)

#finding the best cluster based on the wss
wss=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(milkscaled)
    labels=km.predict(milkscaled)
    wss.append(km.inertia_)
print(wss)
plt.scatter(np.arange(2,10),wss)
plt.plot(np.arange(2,10),wss)
plt.title("Scree Plot")
plt.xlabel("Ks")
plt.ylabel("Wss")
plt.show()

#Best Cluster
km=KMeans(n_clusters=4,random_state=2022)
km.fit(milkscaled)
labels=km.predict(milkscaled)

milk['Cluster']=labels
milk.sort_values('Cluster',inplace=True)


#Calculating the centroids
milk.groupby('Cluster').mean()



          