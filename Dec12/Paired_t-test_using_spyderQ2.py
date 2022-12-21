import pandas as pd
from scipy.stats import ttest_rel

rheumatic= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Rheumatic.csv")


# D = before - after
# H0: D<=0   H1: D <0
ttest_rel(rheumatic['Before'], rheumatic['After'], alternative = "less")

# or 
ttest_rel(rheumatic['After'], rheumatic['Before'], alternative = "greater")