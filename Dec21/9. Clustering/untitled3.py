#####   IRIS dataset  #####
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from  sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris= pd.read_csv("iris.csv")
print(iris)

pca = PCA()
scaler= StandardScaler()
iris_num=iris.drop('Species',axis=1)
iris_scaled=scaler.fit_tansform(iris_num)

prin_comp=pca.fit_transform(iris_scaled)

print(pca.explained_variance_ratio_*100)
sns.scatterplot(data=iris,x='Sepal.Length',y='Sepal.Width',hue='Species')
plt.title("Scatter Plot")
