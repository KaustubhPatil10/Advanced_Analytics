import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
from sklearn.preprocessing import PolynomialFeatures



pizza = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\pizza.csv") 


lr = LinearRegression()

X= pizza[['Promote']]  
y= pizza['Sales'] 
poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(X)
lr.fit(X_poly, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X_poly)
print(r2_score(y, y_pred))


########Insute_auto################
insure = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Insure_auto.csv") 


lr = LinearRegression()

X= insure[['Home','Automobile']]  
y= insure['Operating_Cost'] 
poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(X)
lr.fit(X_poly, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X_poly)
print(r2_score(y, y_pred))

####################### Boston #######################
boston = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Boston.csv") 

X=boston.drop('medv',axis=1)

y = boston['medv']  
lr = LinearRegression()
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

# degree = 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
print(poly.get_feature_names_out())


lr.fit(X_poly, y)
print(lr.intercept_)
print(lr.coef_) 

#################### Concrete Data #############################


concrete = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Cases\Concrete Strength\Concrete_Data.csv") 

X=concrete.drop('Strength',axis=1)
lr = LinearRegression()


y = concrete['Strength']  


poly = PolynomialFeatures(degree = 4)   
#try with every degree 1,2,3,4.
X_poly = poly.fit_transform(X)
print(poly.get_feature_names_out())

lr.fit(X_poly, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X_poly)
print(r2_score(y, y_pred))

#degree 1 = 0.6155198704142721
#degree 2 = 0.8105898913292107
#degree 3 = 0.9254947143090049
#degree 4 = 0.979348231684137       




