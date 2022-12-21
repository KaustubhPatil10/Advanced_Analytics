import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.chdir(r"C:\Kaustubh Vaibhav\Advance Analystics\Day1")
cars93=pd.read_csv(r"Cars93Missing.csv")

print(cars93.info())

cts=cars93['Type'].value_counts()
cts.plot(kind='bar')
plt.show()

#Matplotlib
plt.bar(cts.index,cts)
plt.show() 

#Seaborm

cts1=cts.reset_index()
cts1.columns=['Type','Count']
sns.barplot(data=cts1, x='Type',y='Count')
plt.show()

#Histogram Using price column
cars93['Price'].plot(kind='hist')
plt.show()

cars93['Price'].plot(kind='hist',bin=15)
plt.show()

#matplotlib
plt.hist(cars93['Price'], bins=15)
plt.show()




#Seaborn
sns.histplot(data=cars93,x='Price',bins=15)
plt.show()



#Density plot / Distubution Plot
cars93['Price'].plot(kind='kde')
plt.show()


#Seaborn
sns.kdeplot(data=cars93,x='Price')
plt.show()

###Scatter Plot
cars93.plot(kind='Scatter',x='EngineSize',y='MPG.highway')
plt.title("Scatter plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

#Matplotlib
plt.scatter(cars93['EngineSize'],cars93["MPG.highway"])
plt.title("Scatter plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

#seaborn
sns.scatterplot(data=cars93,x='EngineSize',y='MPG.highway')
plt.title("Scatter plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()


no_bags=cars93[cars93["AirBags"] == "None"]

plt.scatter(no_bags['EngineSize'],no_bags["MPG.highway"],
            label="No Airbags")
driver=cars93[cars93["AirBags"] == "Driver only"]
plt.scatter(driver['EngineSize'],driver["MPG.highway"],
            label="Driver Only")
d_p=cars93[cars93["AirBags"] == "Driver & Passenger"]
plt.scatter(d_p['EngineSize'],d_p["MPG.highway"],
            label="Driver & Passenger")
plt.legend(loc="best")
plt.title("Scatter plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

#Seaborn


sns.scatterplot(data=cars93,x='EngineSize',y='MPG.highway',hue="AirBags")
plt.title("Scatter plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

#Box Plot
cars93["Price"].plot(kind="box")
plt.title("Box Plot")
plt.show()

cars93["EngineSize"].plot(kind="box")
plt.title("Box Plot")
plt.show()

#Matplotlib
plt.boxplot(cars93["Price"])
plt.title("Box Plot")
plt.show()

#seaborn
sns.boxplot(y='Price',data=cars93)
plt.show()

sns.boxplot(x='AirBags',y='Price',data=cars93)
plt.show()

sns.boxplot(x='DriveTrain',y='Price',data=cars93)
plt.show()


#Facet Grid
g=sns.FacetGrid(cars93,col="AirBags")
g=g.map(plt.scatter,"EngineSize","MPG.highway")
plt.show()

#Subplot
plt.subplot(1,2,1)
sns.boxplot(y='Price',data=cars93)
plt.title("Box Plot")

plt.subplot(1,2,2)
sns.histplot(data=cars93,x='Price',bins=8)
plt.title("Histogram")
plt.tight_layout()
plt.show()

#------------------------------------------

plt.subplot(2,2,1)
sns.boxplot(y='Price',data=cars93)
plt.title("Box Plot")

plt.subplot(2,2,2)
sns.histplot(data=cars93,x='Price',bins=8)
plt.title("Histogram")
plt.tight_layout()



plt.subplot(2,2,3)
sns.boxplot(x='AirBags',y='Price',data=cars93)
plt.title("Box Plot")

plt.subplot(2,2,4)
sns.scatterplot(data=cars93,x='EngineSize',y='MPG.highway')
plt.title("ScatterPlot")
plt.tight_layout()
plt.show()


#-------------------
#Joint plot 
sns.jointplot(data=cars93,x="EngineSize",y="MPG.highway")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()



