import os
os.chdir("C:/Users/hp/Documents")

import numpy as np 
import pandas as pd

import warnings
warnings.filterwarnings('ignore')
pd.set_option('max_column', None)


df = pd.read_csv("Week1.csv", na_values=['?', None])



# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):
     # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The Diabetes dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

percent_missing(df)




# Let's now find  which column(s) has missing values
n= df.isna().sum()
print(n)



#let's find  columns with more than 30% missing values
t= (n/df.shape[0])*100
print(t)





def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # dtype of missing values
    mis_val_dtype = df.dtypes

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns




# let's drop columns with more than 30% missing values
df_clean = df.drop(['Nb of sec with 37500B < Vol UL', 'Nb of sec with 6250B < Vol UL < 37500B', 'Nb of sec with 125000B < Vol DL', 
                    'TCP UL Retrans. Vol (Bytes)', 'Nb of sec with 31250B < Vol DL < 125000B','Nb of sec with 1250B < Vol UL < 6250B',
                   'Nb of sec with 1250B < Vol UL < 6250B','TCP DL Retrans. Vol (Bytes)','Nb of sec with 6250B < Vol DL < 31250B',
                   'HTTP UL (Bytes)','HTTP DL (Bytes)'],axis=1)


print(f" There are now {df_clean.shape[0]} rows and {df_clean.shape[1]} columns")




#fix the missing values
def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]

def fix_missing_bfill(df, col):
    df[col] = df[col].fillna(method='bfill')
    return df[col]
    
    
    
    
    
 df_clean['columns'] = df_clean['columns'].fillna(df_clean['columns'].median())
 df_clean['columns'] = df_clean['columns'].fillna(df_clean['columns'].mean())  
    
 
 
 #Scaling
 
 data_scal = (df_clean-df_clean.min())/(df_clean.max()-df_clean.min())
 
 
 
 
 #Normalize
 from sklearn.preprocessing import Normalizer

def normalizer(df):
    norm = Normalizer()
    # normalize the exponential data with boxcox
    normalized_data = norm.fit_transform(df)
    
    
    
  #Extraction of dataframe
  !mkdir "csv"
df_clean.to_csv('csv/df_clean.csv', index=False)

  
