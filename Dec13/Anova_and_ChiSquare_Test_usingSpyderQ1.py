import pandas as pd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

cars = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Cars93.csv")
#=========================================
###########  ANNOVA #######################

# is price influenced by type?
# annova bcoz numrical to categorical
cars_ols = ols('Price ~ Type', data = cars).fit()
table = anova_lm(cars_ols, typ = 2)
print(table)
#conclusion: price is influenced.



# is price influenced by airbags?
cars_ols = ols('Price ~ AirBags', data = cars).fit()
table = anova_lm(cars_ols, typ = 2)
print(table)
#conclusion: price is influenced.



# is price influenced by driver train
cars_ols = ols('Price ~ DriveTrain', data = cars).fit()
table = anova_lm(cars_ols, typ = 2)
print(table)
#conclusion: price is influenced.


#==============================
########### CHI-SQUARE ####################

#are types and airbags related?
# chi-square test is used bcoz both are categorical variables.
ctab = pd.crosstab(cars['Type'], cars['AirBags'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)


#are types and DriveTrain related?
ctab = pd.crosstab(cars['Type'], cars['DriveTrain'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)

#are types and Origin related?
ctab = pd.crosstab(cars['Type'], cars['Origin'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)

#========================================












