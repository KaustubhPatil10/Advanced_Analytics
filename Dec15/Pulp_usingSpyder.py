import pulp as p
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns 

a = np.array([2,5,6,7,10])
b = np.array([30,24,20,17,7])
np.cov(a,b)

pizza = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\pizza.csv")

pizza['Promote'].cov(pizza['Sales'])

np.cov(pizza['Promote'], pizza['Sales'])

# Variance Covariance Matrix
np.cov(pizza['Promote'], pizza['Sales'])
pizza.cov()


#Correlation
pizza['Promote'].corr(pizza['Sales'])

pizza['Promote'].corr(pizza['Promote'])

#Correlation matrix
pizza.corr()
np.corrcoef(pizza['Promote'], pizza['Sales'])

sns.scatterplot(data = pizza, x= 'Promote', y = 'Sales')
plt.show()

############### insure auto #########

insure = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Insure_auto.csv")

insure['Home'].corr(insure['Automobile'])

insure['Home'].corr(insure['Operating_Cost'])

insure['Automobile'].corr(insure['Operating_Cost'])

# or
insure.corr()

#scatter plot
sns.scatterplot(data = insure, x= 'Home', y = 'Operating_Cost')
plt.show()

#heatmap
sns.heatmap(
    insure.corr(),
    xticklabels = insure.corr().columns,
    yticklabels = insure.corr().columns,
    annot = True) # if written FALSE will not show values in the plot.
plt.show()

#pairplot
sns.pairplot(insure)
plt.show()

#kde shows density plot
sns.pairplot(insure,diag_kind = 'kde')
plt.show()

################# iris ############################

iris = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\iris.csv")

iris.corr()

sns.heatmap(
    iris.corr(),
    xticklabels = iris.corr().columns,
    yticklabels = iris.corr().columns,
    annot = True) # if written FALSE will not show values in the plot.
plt.show()


############### boston ###############

boston = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Boston.csv")

boston.corr()


sns.heatmap(
    boston.corr(),
    xticklabels = boston.corr().columns,
    yticklabels = boston.corr().columns,
    annot = True) # if written FALSE will not show values in the plot.
plt.tight_layout()
plt.show()

sns.pairplot(boston,diag_kind = 'kde')
plt.show()
