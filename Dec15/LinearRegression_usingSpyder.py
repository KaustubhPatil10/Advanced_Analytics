import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 

pizza = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\pizza.csv")

lr = LinearRegression()

X = pizza[['Promote']]  # when given double square brackets we get dataframes.
y = pizza['Sales']       # single bracket gives series.
#type(X)        // to get the dataframe .
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_)            


#yi^ 
y_pred = lr.predict(X)

#numerator = np.sum((y - y_pred)**2)
#denominator = np.sum((y - y.mean())**2)
#1 - (numeartor/denominator)

print(r2_score(y, y_pred))

##################### insure_auto ######################

insure = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Insure_auto.csv")




X = insure[['Home']]  # when given double square brackets we get dataframes.
y = insure['Operating_Cost']  

lr.fit(X, y)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))





X = insure[['Automobile']]        # when given double square brackets we get dataframes.
y = insure['Operating_Cost']  

lr.fit(X, y)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))


X=insure[['Home','Automobile']] 
y = insure['Operating_Cost']  
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

##############Boston###############
boston = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Boston.csv")
#X=boston.iloc[:,:-1]
#or
X=boston.drop('medv',axis=1)

y = boston['medv']  
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X)
print(r2_score(y, y_pred))



