#from scipy.cluster.hierarchy import linkage, dendrogram 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 

concrete = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Cases\Concrete Strength\Concrete_Data.csv",
                       index_col = 0)

scaler = StandardScaler()
concretescaled = scaler.fit_transform(concrete)

#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(concretescaled)
    labels=km.predict(concretescaled)
    sil.append(silhouette_score(concretescaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

## Creating clusters with  best k
km=KMeans(n_clusters=best_k,random_state=2022)
km.fit(concretescaled)
labels=km.predict(concretescaled)

concrete['Cluster'] = labels
concrete['Cluster'] = concrete['Cluster'].astype('category')

concrete = pd.get_dummies(concrete,drop_first= True)
 

#======================= Boston ==============================
X = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Boston.csv")

scaler = StandardScaler()
Xscaled = scaler.fit_transform(X)




#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(Xscaled)
    labels=km.predict(Xscaled)
    sil.append(silhouette_score(Xscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

km=KMeans(n_clusters=best_k,random_state=2022)
km.fit(Xscaled)
labels=km.predict(Xscaled)

X['Cluster'] = labels
X['Cluster'] = X['Cluster'].astype('category')

boston_X = pd.get_dummies(X,drop_first= True)
 
############## after clustering 
lr = LinearRegression()
boston_X=X.drop('medv',axis=1)

y = X['medv']  
lr.fit(boston_X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(boston_X)
print(r2_score(y, y_pred))


















