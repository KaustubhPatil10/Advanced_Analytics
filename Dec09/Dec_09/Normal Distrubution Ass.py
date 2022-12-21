from scipy.stats import norm 

import pandas as pd 
#Question 1

norm.cdf(58,64,4)

#Question 2
norm.sf(200,180,30)

# Normal Distrbution 
norm.ppf(0.95,100,15)

#Question 
norm.sf(2000,1678,500)

norm.ppf(0.9,1678,500)

norm.cdf(1900,1678,500)-norm.cdf(1000,1678,500)

#QUESTION 3
norm.ppf(0.98,313,57)

norm.ppf(0.90,93,22)

norm.sf(450,313,57)+norm.sf(150,93,22)-norm.sf(450,313,57)*norm.sf(150,93,22)