import pandas as pd
from scipy.stats import ttest_1samp,bartlett,ttest_ind

cars = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Datasets\Cars93.csv")

usa = cars[ cars['Origin']== "USA"]
non_usa = cars[ cars['Origin']== "non-USA"]

bartlett(usa['Price'],non_usa['Price'])

ttest_ind(usa['Price'], non_usa['Price'],
          equal_var = False)

#ttest_ind(usa['Price'], non_usa['Price'],
 #         alternative = "greater",
  #        equal_var = False)

cars.groupby('Origin')['Price'].mean()


###################  Man.trans.avail ###########################

yes_man = cars[ cars['Man.trans.avail']== "Yes"]
no_man = cars[ cars['Man.trans.avail']== "No"]

bartlett(yes_man['Price'],no_man['Price'])

ttest_ind(yes_man['Price'], no_man['Price'],
          equal_var = True)
