import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



fifa = pd.read_csv('C:\\Users\\user\\.spyder-py3\\FIFA\\FIFA.csv')

#SEE IF NaN VALUES EXISTS
print(fifa.isna().any())

print(fifa.info())
print(fifa.head())
print(fifa.dtypes)
print(fifa.describe())




#AGE BREAKDOWN
print(fifa['Age'].value_counts())
#BAR GRAPH OF COUNT BY AGE
ax = sns.catplot(x='Age',kind='count',data=fifa,orient="h",height=30,aspect=1)
ax.fig.suptitle('Age Count')
ax.fig.autofmt_xdate()










#%%