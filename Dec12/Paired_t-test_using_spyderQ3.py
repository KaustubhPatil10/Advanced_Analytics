import pandas as pd
from scipy.stats import ttest_rel

plaque= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Plaque.csv")


########## Plaque ########################

plaq_pivot = pd.pivot_table(plaque, index=['Id','product'],
                            columns='trt',values='score')

plaq_pivot = plaq_pivot.reset_index()

P1= plaq_pivot[plaq_pivot['product']=="P1"]
ttest_rel(P1['Before'], P1['After'], alternative = "greater")

P1= plaq_pivot[plaq_pivot['product']=="P2"]
ttest_rel(P1['Before'], P1['After'], alternative = "greater")

P1= plaq_pivot[plaq_pivot['product']=="P3"]
ttest_rel(P1['Before'], P1['After'], alternative = "greater")

