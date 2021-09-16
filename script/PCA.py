

import numpy as np 
import pandas as pd

import warnings
warnings.filterwarnings('ignore')
pd.set_option('max_column', None)

df = pd.read_csv("df", na_values=['?', None])
from sklearn.preprocessing import scale #data scaling
x = scale(df)


#PCA
from sklearn import decomposition #PCA
pca= decomposition.PCA(n_components=3)
pca.fit(x)



#import pandas as pd
scores= pca.transform(x)
scores_df =pd.DataFrame(scores,columns=['PC1','PC2','PC3'])
scores_df





#Retrieve loading value


loadings=pca.components_.T
df_loadings=pd.DataFrame(loadings,columns=['PC1','PC2','PC3'],index=df.columns)
df_loadings



#Culmulative variance
explained_variance =pca.explained_variance_ratio_
explained_variance
explained_variance =np.insert(explained_variance,0,0)
cumulative_variance = np.cumsum(np.round(explained_variance,decimals=3))
pc_df=pd.DataFrame(['','PC1','PC2','PC3'],columns=['PC'])
explained_variance_df=pd.DataFrame(explained_variance,columns=['Explained Variance'])
cumulative_variance_df=pd.DataFrame(cumulative_variance,columns=['Cumulative Variance'])
df_explained_variance= pd.concat([pc_df,explained_variance_df,cumulative_variance_df],axis=1)
df_explained_variance



#Make plot
def plot_bar(df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
    plt.figure(figsize=(12, 7))
    sns.barplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks( fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.show()



plot_bar(df_explained_variance,'PC','Explained Variance','Explained Variance','PC','Explained Variance




#3D plot
import plotly.express as px
fig=px.scatter_3d(scores_df,x='PC1',y='PC2',z='PC3')
fig.show()