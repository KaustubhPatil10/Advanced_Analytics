import pandas as pd
from scipy.stats import ttest_1samp,bartlett,ttest_ind

soporific = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Soporific.csv")

bartlett(soporific['Drug A'],soporific['Drug B'])

ttest_ind(soporific['Drug A'], soporific['Drug B'], equal_var = True)


##########################



