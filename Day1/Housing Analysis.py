import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.chdir(r"C:\Kaustubh Vaibhav\Advance Analystics\Day1")
housing=pd.read_csv("Housing.csv")


print(housing.info())

#Skewness

housing['price'].skew()

#Kurtosis

housing["price"].kurtosis()

#Histogram
housing['price'].plot(kind='hist')
plt.show()

#matplotlib
plt.hist(housing['price'], bins=15)
plt.show()




#Seaborn
sns.histplot(data=housing,x='price',bins=15)
plt.show()



#Scatter Plot
#seaborn
sns.scatterplot(data=housing,x='lotsize',y='price',hue="airco")
plt.title("Scatter plot")
plt.xlabel("Lotsize")
plt.ylabel("Price")
plt.show()

housing.plot(kind='Scatter',x='lotsize',y='price')
plt.title("Scatter plot")
plt.xlabel("LOTSIZE")
plt.ylabel("PRICE")
plt.show()

#Matplotlib
plt.scatter(housing['lotsize'],housing["price"])
plt.title("Scatter PLOT")
plt.xlabel("LOTSIZE")
plt.ylabel("PRICE")
plt.show()


#BOX PLOT
#seaborn
sns.boxplot(x='bathrms',y='lotsize',data=housing)
plt.show()

#python
housing["price"].plot(kind="box")
plt.title("Box Plot")
plt.show()


#Matplotlib
plt.boxplot(housing["price"])
plt.title("Box Plot")
plt.show()


#Facet Grid
g=sns.FacetGrid(housing,col="bathrms")
g=g.map(plt.scatter,"price","lotsize")
plt.show()


#JOINT PLOT
sns.jointplot(data=housing,x="lotsize",y="price")
plt.xlabel("LOTSIZE")
plt.ylabel("PRICE")
plt.show()


#SUBPLOT

plt.subplot(2,2,1)
sns.boxplot(y='price',data=housing)
plt.title("Box Plot")


plt.subplot(2,2,2)
sns.histplot(data=housing,x='price')
plt.title("Histogram")



plt.subplot(2,2,3)
sns.scatterplot(data=housing,x='lotsize',y='price',hue="airco")
plt.title("ScatterPlot")



plt.subplot(2,2,4)
sns.boxplot(y='bathrms',data=housing)
plt.title("Box Plot")
plt.tight_layout()
plt.show()