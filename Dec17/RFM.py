import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



rfm = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\rfm_data_customer.csv",
                   index_col = 0)


rfm.drop(columns=['most_recent_visit'],inplace=True)
rfm.info()
scaler = StandardScaler()
rfmscaled = scaler.fit_transform(rfm)

#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(rfmscaled)
    labels=km.predict(rfmscaled)
    sil.append(silhouette_score(rfmscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)





