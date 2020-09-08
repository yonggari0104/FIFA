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
