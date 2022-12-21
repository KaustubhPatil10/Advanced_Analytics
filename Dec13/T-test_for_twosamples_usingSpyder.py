import pandas as pd
from scipy.stats import ttest_1samp,bartlett,ttest_ind

puromycin = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Puromycin.csv")


treated = puromycin[ puromycin['state']== "treated"]


untreated = puromycin[ puromycin['state']== "untreated"]

bartlett(treated['rate'],untreated['rate'])

ttest_ind(treated['rate'], untreated['rate'], equal_var = True)


##########################



