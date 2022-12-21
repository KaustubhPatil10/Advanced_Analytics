import pandas as pd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

plantgrowth = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\PlantGrowth.csv")

plant_ols = ols('weight ~ group', data = plantgrowth).fit()
table = anova_lm(plant_ols, typ = 2)
print(table)


compare =pairwise_tukeyhsd(plantgrowth['weight'],
                           plantgrowth['group'],alpha = 0.05)

dd = pd.DataFrame(compare._results_table.data)
dd

plantgrowth.groupby('group')['weight'].mean()