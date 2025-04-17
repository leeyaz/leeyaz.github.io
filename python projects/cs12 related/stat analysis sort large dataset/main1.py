import pandas as pd
import numpy as np

df = pd.read_csv(r"stat analysis sort large dataset/global_spice_consump.csv") #(question 1) read_csv

#we know from below that these columns have the same value for the entire dataset
'''
In:
    repeats = df.loc[
        (df['Domain Code'] != 'TCL') | 
        (df['Domain'] != 'Crops and livestock products') | 
        (df['Unit'] != 't')] 
    print(repeats)

Out:
    []
'''

#dropping columns thats info idk what to do with
df = df.drop(columns=['Domain Code','Domain','Area Code (M49)','Element Code','Item Code (CPC)','Unit'])

#checking for NaNs (question 2)
any_missing = df.isna().nunique() #.isna() returns True or False whether its NaN or not for each value. .nunique() returns number of distinct elements.
#print(any_missing) #all return 1, thus only one bool gets returned from df.isna(), which is False (you'd know from running df.na()). Therefore there are no missing values.

#statistics (going to use what's convenient) (question #3)
descr = df.describe(include=np.number).astype('int')
descr.rename(index={'50%':'median'}, inplace=True) #renaming %50 as median because i want to
print(descr)

#sort based on criterion (question #4)
#criteria: Area == Canada
inCanada = df.loc[df['Area'] == 'Canada'] #locate only the ones in Canada
inCanada = inCanada.drop(columns='Area') #feels redundant to have Area=Canada for all so dropping that column

#export to new csv (question #5)
inCanada.to_csv('stat analysis sort large dataset/canada_spice_consump.csv', index=False) #index=False because no need for indexes from prev dataset

#spices that Canada actually consumes (Consumption is positive) (extra)
canadaConsumes = inCanada.loc[inCanada['Consumption']>0]
spice = canadaConsumes['Item'].unique() #returns array

#question 4 ig
consumption = { #spice: (year: consumption) #1st dict
    item: dict( #2nd inner dict
        canadaConsumes.loc[canadaConsumes['Item'] == item][['Year', 'Consumption']] #when 'Item' == item (from the loop) get 'Year' and 'Consumption
        .set_index('Year')['Consumption'] #'Year' is the key and 'Consumption' is the value
    )
    for item in spice
}

consumption_df = pd.DataFrame.from_dict(consumption).rename_axis('Year') #make dict into dataframe
consumption_df = consumption_df.sort_values(by='Year') #sort by order of year (cant mesh with one on top because axis got to be renamed first >-<) (question #4)
consumption_df2 = consumption_df.fillna('No Info') #fill missing values with 'No Info' (diff var from before because empty values are better for .describe()) (question #2)
consumption_df2.to_csv('stat analysis sort large dataset/canadian consumption of spices based on years in tonnes.csv', index=True) #make dataframe a csv (keep index, it is year) (question #5)

#description (question #3)
desc2 = consumption_df.describe(include='all') #used consumption_df instead of consumption_df2 because strings interfere with .describe()
desc2_df = pd.DataFrame(desc2).rename_axis('Stats') #.describe() series turns into a dataframe
desc2_df.to_csv('stat analysis sort large dataset/description on ccosboyit (spices in tonnes).csv', index=True) #which turns into a csv
