############# WINE ############
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from  sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
wine= pd.read_csv("wine.csv")
print(wine)

pca = PCA()
scaler= StandardScaler()
pipe= Pipeline([('' , )])


prin_comp=pca.fit_transform(wine_scaled)

print(pca.explained_variance_ratio_*100)
sns.scatterplot(data=wine,x='Sepal.Length',y='Sepal.Width',hue='Species')
plt.title("Scatter Plot")




