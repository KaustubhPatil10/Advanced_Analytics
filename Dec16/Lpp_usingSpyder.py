import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
import os


###################### exp_salaries ###################
exp_sals = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Exp_Salaries.csv")

dum_sals = pd.get_dummies(exp_sals, drop_first = True)


lr = LinearRegression()

X=dum_sals.drop('Salary',axis=1)

y = dum_sals['Salary']  
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

####################   sals to predict ###################
# Generating the predictions.
SalsToPred = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\SalsToPredict.csv")

#SalsToPred.columns
dum_pred = pd.get_dummies(SalsToPred, drop_first = True)
predictions = lr.predict(dum_pred)

######## Wedding#######

wedding = pd.read_excel(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Weddings.xlsx",usecols="A:F",skiprows=2)

X= wedding[['Wedding cost']]  
y= wedding['Attendance'] 
lr = LinearRegression()
lr.fit(X, y)
print(lr.intercept_)       # b0 - intercept.
print(lr.coef_) 
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

################### credit approval decisions ################





















