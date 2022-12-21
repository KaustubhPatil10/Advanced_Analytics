import pandas as pd
from scipy.stats import ttest_1samp,bartlett,ttest_ind

co2= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\CO2.csv")


ttest_1samp(co2['uptake'],popmean = 30, alternative = "two-sided")

ttest_1samp(co2['uptake'],popmean = 30, alternative = "greater")
ttest_1samp(co2['uptake'],popmean = 30, alternative = "less")

#pop mean uptake maybe less than 30.

chilled = co2[ co2['Treatment']== "chilled"]


unchilled = co2[ co2['Treatment']== "nonchilled"]

bartlett(chilled['uptake'],unchilled['uptake'])

ttest_ind(chilled['uptake'], unchilled['uptake'], equal_var = True)