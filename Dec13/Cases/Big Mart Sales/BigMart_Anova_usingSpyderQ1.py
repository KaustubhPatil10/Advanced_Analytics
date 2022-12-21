import pandas as pd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import seaborn as sns
from matplotlib import pyplot as plt


train = pd.read_csv(r"C:\Kaustubh Vaibhav\Advance Analystics\Dec13\Cases\Big Mart Sales\train_v9rqX0R.csv")

train['Item_Type'].unique()
len(train['Item_Type'].unique())

######## ANOVA #####################
train_ols = ols('Item_Outlet_Sales ~ Item_Type', data = train).fit()
table = anova_lm(train_ols, typ = 2)
print(table)


#error type bar plot
sns.barplot(data = train, y= "Item_Type" , x = "Item_Outlet_Sales")
plt.show()

#bar plot
# item type
cts = train.groupby('Item_Type')['Item_Outlet_Sales'].mean()
cts1 = cts.reset_index()
sns.barplot(data = cts1, x='Item_Outlet_Sales', y ='Item_Type')
plt.xlabel('Item_Outlet_Sales')
plt.ylabel('Item_Type')
plt.show()

train['Outlet_Type'].unique()

train_ols = ols('Item_Outlet_Sales ~ Item_Type', data = train).fit()
table = anova_lm(train_ols, typ = 2)
print(table)

# conclusion outlet type does influence item sales.

# ========================================
# outlet type
cts = train.groupby('Outlet_Type')['Item_Outlet_Sales'].mean()
cts1 = cts.reset_index()
sns.barplot(data = cts1, x='Item_Outlet_Sales', y ='Outlet_Type')
plt.xlabel('Mean Item Sales')
plt.ylabel('Outlet Types')
plt.show()

train_ols = ols('Item_Outlet_Sales ~ Outlet_Type', data = train).fit()
table = anova_lm(train_ols, typ = 2)
print(table)

#==========================================
# fat content
cts = train.groupby('Item_Fat_Content')['Item_Outlet_Sales'].mean()
cts1 = cts.reset_index()
sns.barplot(data = cts1, x='Item_Outlet_Sales', y ='Item_Fat_Content')
plt.xlabel('Mean Item Sales')
plt.ylabel('Fat Content')
plt.show()


train_ols = ols('Item_Outlet_Sales ~ Item_Fat_Content', data = train).fit()
table = anova_lm(train_ols, typ = 2)
print(table)

#============================================
#replacing names of fat content.
train['Item_Fat_Content'].value_counts()

train['Item_Fat_Content'].replace({'low fat':'Low Fat','LF':'Low Fat',
                                   'reg':'Regular'}, inplace = True)

cts = train.groupby('Item_Fat_Content')['Item_Outlet_Sales'].mean()
cts1 = cts.reset_index()
sns.barplot(data = cts1, x='Item_Outlet_Sales', y ='Item_Fat_Content')
plt.xlabel('Mean Item Sales')
plt.ylabel('Fat Content')
plt.show()

train_ols = ols('Item_Outlet_Sales ~ Item_Fat_Content', data = train).fit()
table = anova_lm(train_ols, typ = 2)
print(table)

#conclusion : fat content  does not affect sales

#==========================================
# does item type influence item MRP
train_ols = ols('Item_MRP ~ Item_Type', data = train).fit()
table = anova_lm(train_ols, typ = 2)
print(table)

#conclusion : item type influences item MRP

cts = train.groupby('Item_Type')['Item_MRP'].mean()
cts1 = cts.reset_index()
sns.barplot(data = cts1, x='Item_MRP', y ='Item_Type')
plt.xlabel('Mean Item MRP')
plt.ylabel('Item Type')
plt.show()

