import pandas as pd
from scipy.stats import ttest_rel

anorexia= pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\anorexia.csv")

cont = anorexia[anorexia['Treat']=="Cont"]
ttest_rel(cont['Prewt'], cont['Postwt'], alternative = "less")


cbt = anorexia[anorexia['Treat']=="CBT"]
ttest_rel(cbt['Prewt'], cbt['Postwt'], alternative = "less")


ft = anorexia[anorexia['Treat']=="FT"]
ttest_rel(ft['Prewt'], ft['Postwt'], alternative = "less")