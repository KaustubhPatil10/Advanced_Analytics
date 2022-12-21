import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(r"C:\Kaustubh Vaibhav\Advance Analystics\Day1")
cars93=pd.read_csv(r"Cars93Missing.csv")
print(cars93.shape)
print(cars93.info())

cars93['Price'].mean()
cars93['Price'].median
cars93['Price'].mean()

cars93['Price'].quantile(q=0.25)
cars93['Price'].quantile(q=np.array([0.25,0.5,0.75]))

#cars93['Price'].plot(kind='box')
#plt.show()

cars93['Price'].std()

cars93['Price'].var()

cv=cars93['Price'].std()/cars93['Price'].mean()
print(cv)

from scipy.stats import skew
skew(cars93['Price'])
cars93['Price'].skew()

from scipy.stats import kurtosis
kurtosis(cars93['Price'],fisher=True)
cars93['Price'].kurtosis()

#-----------GROUP BY Aggregation---------------------------

cars93.groupby('AirBags')['Price'].mean()



#Matloblib

cts=cars93.groupby('AirBags')['Price'].mean()
plt.bar(cts.index,cts)
plt.ylabel("Mean Price")
plt.show()



