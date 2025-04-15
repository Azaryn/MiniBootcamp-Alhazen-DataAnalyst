import numpy as np
import pandas as pd
from termcolor import cprint

def pembatas():
    print(" ")

# series
pop_g7 = pd.Series([39.467, 68.951, 84.940, 58.665, 124.061, 67.511, 334.523]) 
print(pop_g7)
print("Type Data: ",pop_g7.values)

pop_g7.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
pembatas()
print(pop_g7)

# pd.Series({
#     'Canada': 39.467,
#     'France': 68.951,
#     'Germany': 84.940,
#     'Italy': 58.665,
#     'Japan': 124.061,
#     'United Kingdom': 67.511,
#     'United States': 334.523,
# }, name='G7 Population in millions')
pembatas()
pop_g7 = pd.Series(
    [39.467, 68.951, 84.940, 58.665, 124.061, 67.511, 334.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G7 Population in millions'
)
print(pop_g7)
pembatas()
print(pd.Series(pop_g7, index=['France', 'Germany', 'Italy', 'Spain']))

#Indexing
pembatas()
print(pop_g7)
pembatas()
print(pop_g7[['Italy', 'Canada']])

pembatas()
print("iloc index 0: ", pop_g7.iloc[0])
print("Value colom US: ", pop_g7['United States'])
print(pop_g7.iloc[[0, 4]]) #melihat index 0 dan 4

pembatas() #Melihat index dari colum france sampai japan
print(pop_g7['France': 'Japan'])

#Boolean
pembatas()
print(pop_g7[pop_g7 < 80])

print(pop_g7[(pop_g7 > 50) & (pop_g7 < 80)])

#Series Modification
print(pop_g7)
pembatas()
pop_g7['United States'] = 339.00
print(pop_g7)

#DataFrame
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
pembatas()
print(df)

pembatas()
cprint("Columns:", "red")
print(df.columns)

pembatas()
cprint("Index:", "red")
print(df.index)

pembatas()
print(df.info())

pembatas()
print(df.size)

pembatas()
print(df.describe())

pembatas()
print(df.dtypes)

pembatas()
print(df.dtypes.value_counts())

#Indexing 
pembatas()
print(df.loc['Canada'])

pembatas()
print(df.iloc[-1])

pembatas()
print(df['Population'].to_frame())

pembatas()
print(df[['Population', 'GDP']])

# Slicing
pembatas()
print(df[1:4])

pembatas()
print(df.loc['France': 'United Kingdom'])

pembatas()
print(df.loc['France': 'United Kingdom', ['Population', 'HDI', 'Continent']])

#Conditional
pembatas()
print(df[df['Continent'] == 'Europe'])

pembatas()
print(df[df['Population'] > 100])

pembatas()
print(df.loc[df['Population'] > 80, ['Population', 'Continent']])

# Dropping Method
pembatas()
print(df.drop(['Canada', 'France']))

pembatas()
print(df.drop(columns=['Population', 'HDI']))

pembatas()
print(df.drop(['Italy', 'Canada'], axis=0))

pembatas()
print(df.drop(columns=['Population', 'HDI']))

#Columns Rename
df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC'
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    })