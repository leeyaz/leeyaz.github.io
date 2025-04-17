import pandas as pd

df1 = pd.read_csv(r'stat analysis sort large dataset/canadian consumption of spices based on years.csv') #read csv

#fill the missing values
df1 = df1.fillna('No Info')
#df1=df1.dropna() <-- want to keep rows so no this

#description
desc1 = df1.describe(include='all')
