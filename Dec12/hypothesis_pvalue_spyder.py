import pandas as pd
from scipy.stats import ttest_1samp

pg= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\PlantGrowth.csv") 

ttest_1samp(pg['weight'],popmean = 6, alternative = "two-sided")

ttest_1samp(pg['weight'],popmean = 6, alternative = "greater")

ttest_1samp(pg['weight'],popmean = 6, alternative = "less")

