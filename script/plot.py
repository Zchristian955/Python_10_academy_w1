import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#histogramm
df =pd.csv('df')

def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
    plt.figure(figsize=(9, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()



##Heatmap
f,ax=plt.subplots(figsize=(14,14))
sns.heatmap(df.corr(),annot=True, linewidths=5, fmt='.1f', ax=ax)

###
#I need to convert our categorical coumns, into numerical by using hot encoding on the dataset


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler



for column in df.columns:
  if df[column].dtype == np.int64 or df[column].dtype == np.float64:
    continue
  df[column] = LabelEncoder().fit_transform(df[column])

high_corr_data = df.corr()
high_corr_columns = high_corr_data.index[abs(high_corr_data['Bearer Id'])>=0.5]
high_corr_columns


plt.figure(figsize=(16,8))
sns.heatmap(df[high_corr_columns].corr(), annot=True, cmap="coolwarm")



    