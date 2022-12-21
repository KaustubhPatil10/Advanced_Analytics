import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(r"C:\Kaustubh Vaibhav\Advance Analystics\Day1")
cars93=pd.read_csv(r"Cars93Missing.csv")
print(cars93.info())

#Probability Distrubution of Type & AirBAgs
cars93['Type'].value_counts(normalize=True) 
cars93['AirBags'].value_counts(normalize=True)


#Joint Probability of Type & AirBags
pd.crosstab(cars93['Type'],cars93['AirBags'],normalize='all',margins=True)

#Conditional Probability Distrubution
pd.crosstab(cars93['Type'],cars93['AirBags'],normalize='columns',margins=True)

