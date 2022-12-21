import pandas as pd
import numpy as np
x1=np.array(['A','A','A','B','B','B','C','C'])
x2=np.array(['P','Q','P','Q','P','P','Q','Q'])

#Crosstab
pd.crosstab(index=x1,columns=x2)

#joint Probability distribution
pd.crosstab(index=x1,columns=x2,normalize='all',margins=True)

#Conditional probability distribution for rows
pd.crosstab(index=x1,columns=x2,normalize='index',margins=True)

#Conditional probability distribution for columns
pd.crosstab(index=x1,columns=x2,normalize='columns',margins=True)
