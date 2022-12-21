import pandas as pd
from scipy.stats import ttest_1samp

indo= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Indometh.csv")


ttest_1samp(indo['conc'],popmean = 0.30, alternative = "two-sided")

ttest_1samp(indo['conc'],popmean = 0.30, alternative = "greater")
ttest_1samp(indo['conc'],popmean = 0.30, alternative = "less")
