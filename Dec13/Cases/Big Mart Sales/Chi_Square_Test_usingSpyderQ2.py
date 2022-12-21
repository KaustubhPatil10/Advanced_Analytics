import pandas as pd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

train = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Dec13\Cases\Big Mart Sales\train_v9rqX0R.csv")

# is fat content related to item type
ctab = pd.crosstab(train['Item_Fat_Content'], train['Item_Type'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)
#conclusion: may be dependent.


# is outlet type related to item type
ctab = pd.crosstab(train['Outlet_Type'], train['Item_Type'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)
#conclusion: may be independent.


# is outlet location type related to item type
ctab = pd.crosstab(train['Outlet_Location_Type'], train['Item_Type'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)
#conclusion: may be independent.

