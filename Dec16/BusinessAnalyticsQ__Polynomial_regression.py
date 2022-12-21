import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
import statsmodels.api as sm

pizza = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\pizza.csv") 

X= pizza[['Promote']]  
X = sm.add_constant(X)
y= pizza['Sales'] 
model = sm.OLS(y,X)
results = model.fit()

print(results.params)
print(results.summary())

#Credit approval
credit = pd.read_excel(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\CreditApprovalDecisions.xlsx",
                       sheet_name = "Data",usecols="A:F",skiprows=2)

X = sm.add_constant(X)
y = pizza['Sales']
model = sm.OLS(y,X)
results = model.fit()

print(results.params)
print(results.summary())

################### Credit Approval Decisions ###############
# same question using different parameters
cred = pd.read_excel(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\CreditApprovalDecisions.xlsx",
                       sheet_name = "Data",usecols="A:F",skiprows=2)

X = cred[['Years of Credit History',
          'Revolving Balance', 'Revolving Utilization']]

X = sm.add_constant(X)
y = cred['Credit Score']
model = sm.OLS(y,X)
results = model.fit()

print(results.params)
print(results.summary())
