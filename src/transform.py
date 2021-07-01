import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data_path = '/home/facundoic/Desktop/GitHub/Repositories/Data-Science-Projects/data/2018.csv'
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
df.sort_values(by=['Total'],ascending=False,inplace=True)

df['Causas'] = [causa.split('.')[1] if '.' in causa else causa for causa in df['Causas'] ]
total_label = [str(num) for num in df.iloc[2:7,4]]
print(df.head(8))

plt.title('Top 5 Causas de muerte en 2018')
labels = df.iloc[2:7,2] + " : " + total_label
plt.pie(df.iloc[2:7,4],labels=labels)
plt.show()