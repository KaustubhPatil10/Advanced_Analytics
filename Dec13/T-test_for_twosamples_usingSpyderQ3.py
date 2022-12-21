import pandas as pd
from scipy.stats import ttest_1samp,bartlett,ttest_ind

house = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Housing.csv")

preferred = house[ house['prefarea']== "yes"]
non_pferred = house[ house['prefarea']== "no"]

bartlett(preferred['price'],non_pferred['price'])

ttest_ind(preferred['price'], non_pferred['price'],
          alternative = "greater",
          equal_var = False)

house.groupby('prefarea')['price'].mean()


############################################

ac = house[ house['airco']== "yes"]
non_ac = house[ house['airco']== "no"]

bartlett(ac['price'],non_ac['price'])

ttest_ind(ac['price'], non_ac['price'],
          alternative = "greater",
          equal_var = False)


house.groupby('airco')['price'].mean()

###################### gas #############################

yes_gas = house[ house['gashw']== "yes"]
no_gas = house[ house['gashw']== "no"]

bartlett(yes_gas['price'],no_gas['price'])

ttest_ind(yes_gas['price'], no_gas['price'],
          equal_var = True)
