import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import os
from sklearn.preprocessing import StandardScaler

milk= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\milk.csv",index_col=0)
scaler=StandardScaler()
scaler.fit(milk)
milkscaled=scaler.transform(milk)


pca=PCA()
prin_comp=pca.fit_transform(milkscaled)

print(milk.shape)
print(prin_comp.shape)

pd_pc=pd.DataFrame(prin_comp,columns=['PC1','PC2','PC3','PC4','PC5'])

pd_pc.var() #or
print(pca.explained_variance_)


#% age variation explained
print(pca.explained_variance_ratio_*100)

#Scree Plot

ys=np.cumsum(pca.explained_variance_ratio_*100)
xs=np.arange(1,6)
plt.plot(xs,ys)
plt.title("Scree PLOT")
plt.xlabel("Principal Components")
plt.ylabel("Cumulative % age variation explained")
plt.show()

##############Biplot######
from pca import pca

milk= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\milk.csv",index_col=0)
scaler=StandardScaler()
scaler.fit(milk)
milkscaled=scaler.transform(milk)
milkscaled=pd.DataFrame(milkscaled,columns=milk.columns,index=milk.index)

model=pca()
results=model.fit_transform(milkscaled)
fig, ax=model.biplot(label=True,legend=False)

#################IRIS#########
iris=pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\iris.csv",index_col=4)

scaler=StandardScaler()
scaler.fit(iris)
irisscaled=scaler.transform(iris)


pca=PCA()
prin_comp=pca.fit_transform(irisscaled)

print(iris.shape)
print(prin_comp.shape)

pd_pc=pd.DataFrame(prin_comp,columns=['PC1','PC2','PC3','PC4'])

pd_pc.var() #or
print(pca.explained_variance_)

#% age variation explained
print(pca.explained_variance_ratio_*100)

pd_pc['Species']= iris['Species']


#Scatter Plot
import seaborn as sns
sns.scatterplot(data=pd_pc, x='PC1',y='PC2',hue='Species')
plt.title("Scatter Plot")
plt.show()

####Wine####

wine=pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\wine.csv")


scaler=StandardScaler()
scaler.fit(wine)
winescaled=scaler.transform(wine)


pca=PCA()
prin_comp=pca.fit_transform(winescaled)

print(wine.shape)
print(prin_comp.shape)

pd_pc=pd.DataFrame(prin_comp,columns=['PC'+str(i) for i in np.arange(1,14)])

pd_pc.var() #or
print(pca.explained_variance_)

#% age variation explained
print(pca.explained_variance_ratio_*100)

pd_pc['Class']= wine['Class']
pd_pc['Class']=pd_pc['Class'].astype('category')


#Scatter Plot
import seaborn as sns
sns.scatterplot(data=pd_pc, x='PC1',y='PC2',hue='Class')
plt.title("Scatter Plot")
plt.show()


#######Train###
train=pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Cases\Big Mart Sales\processed_train.csv")

X=train.drop(['Item_Identifier','Item_Outlet_Sales','Outlet_Identifier'],axis=1)

dum_X=pd.get_dummies(X,drop_first=True)

scaler=StandardScaler()
scaler.fit(dum_X)
winescaled=scaler.transform(dum_X)


pca=PCA()
prin_comp=pca.fit_transform(winescaled)

print(dum_X.shape)
print(prin_comp.shape)

#pd_pc=pd.DataFrame(prin_comp,columns=['PC'+str(i) for i in np.arange(1,14)])

pd_pc.var() #or
print(pca.explained_variance_)

#% age variation explained
print(pca.explained_variance_ratio_*100)
np.cumsum(pca.explained_variance_ratio_*100)

#Scree Plot

ys=np.cumsum(pca.explained_variance_ratio_*100)
xs=np.arange(1,28)
plt.plot(xs,ys)
plt.title("Scree PLOT")
plt.xlabel("Principal Components")
plt.ylabel("Cumulative % age variation explained")

plt.axhline(y=95,color='r',linestyle="--")
plt.show()

####Protein####
protein=pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Protein.csv",index_col=0)



scaler=StandardScaler()
scaler.fit(protein)
proteinscaled=scaler.transform(protein)


pca=PCA()
prin_comp=pca.fit_transform(proteinscaled)

print(protein.shape)
print(prin_comp.shape)

#pd_pc=pd.DataFrame(prin_comp,columns=['PC'+str(i) for i in np.arange(1,14)])

pd_pc.var() #or
print(pca.explained_variance_)

#% age variation explained
print(pca.explained_variance_ratio_*100)
np.cumsum(pca.explained_variance_ratio_*100)

###Biplot####
from pca import pca

protein= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Protein.csv",index_col=0)
scaler=StandardScaler()
scaler.fit(protein)
proteinscaled=scaler.transform(protein)
proteinscaled=pd.DataFrame(proteinscaled,columns=protein.columns,index=protein.index)

model=pca()
results=model.fit_transform(proteinscaled)
fig, ax=model.biplot(label=True,legend=False)


#Finding the best k using  silhouette_score

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
scaler = StandardScaler()
proteinscaled = scaler.fit_transform(X)




#finding the best cluster based on the silhouette
sil=[]
for i in np.arange(2,10):
    km=KMeans(n_clusters=i,random_state=2022)
    km.fit(proteinscaled)
    labels=km.predict(proteinscaled)
    sil.append(silhouette_score(proteinscaled, labels))
print(sil)

#Best Cluster
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

#Genrating the labels corresponding to best k
km=KMeans(n_clusters=best_k,random_state=2022)
km.fit(proteinscaled)
labels=km.predict(proteinscaled)


pd_pc=pd.DataFrame(prin_comp,columns=['PC'+str(i) for i in np.arange(1,10)])

pd_pc['Cluster'] = labels


pd_pc['Cluster']=pd_pc['Cluster'].astype('category')
import seaborn as sns
sns.scatterplot(data=pd_pc, x='PC1',y='PC2',hue='Cluster')
plt.title("Scatter Plot")
plt.show()
