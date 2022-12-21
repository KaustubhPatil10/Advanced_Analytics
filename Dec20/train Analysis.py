import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
import os
from sklearn.preprocessing import StandardScaler

train= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Dec20\train.csv")


X= train.drop(['count','datetime'], axis = 1)
y= train['count'] 

scaler = StandardScaler()
trainscaled = scaler.fit_transform(X)


lr = LinearRegression()
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X)
print(r2_score(y, y_pred))
