import numpy as np
import pandas as pd



data_path = '/home/facundoic/Desktop/GitHub/Repositories/Data-Science-Projects/data/2005.csv'
df = pd.read_csv(data_path,sep=';',encoding='latin-1')


print('-----------------------DATAFRAME INFO--------------------------------')
print(df.info())
print('----------------------UNIQUE VALUES----------------------------------')
print(df[:].nunique())
print('---------------------NULL VALUES-----------------------------------')
print(df.isnull().sum())
print('---------------------DUPLICATED VALUES----------------------------------')
print(df.duplicated(subset=['Grupo']).sum())
print('------------------------------------------------------------------------')
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'Grupo_de_Causas_de_Defunción':'Causas'})

print(df.head())
