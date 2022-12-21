import pandas as pd
from scipy.stats import chi2_contingency

house = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Housing.csv")
 

#crosstab is used as table in Rstudio                   
ctab = pd.crosstab(house['prefarea'], house['gashw'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)
                    