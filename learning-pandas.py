# Introduction with NumPy

# Benifits.. 1) Flexibility of python.. 2) Work with Big data..

from os import cpu_count
import pandas as pd

# Loading data into pandas...

df = pd.read_csv('pokemon_data.csv')  # if in .csv format...



#df_xlsx = pd.read_excel('pokemon_data.xlsx')   # for excels files...
#df = pd.read_csv('pokemon_data.txt', delimiter='\t')   # for tab seperated values...

#print(df)

print(df.head(3))
print(df.tail(3))

print(df.columns)
print(df['Name'][0:5])
print(df.Name)  # another way of doing the same...


print(df[['Name', 'Type 1', 'HP']])

# Read each row..

print(df.iloc[0:4])

# Read a specific location (R,C)

print(df.iloc[2,1])

for index, row in df.iterrows():
    print(index, row['Name'])

print(df.loc[df['Type 1'] == 'Fire'])  

# Sorting/Describing Data...

print(df.describe())
print(df.sort_values('Name', ascending=False))
print(df.sort_values(['Name', 'HP'], ascending=True))
print(df.sort_values(['Name', 'HP'], ascending=[1,0]))  # first one (Name) will go highest to lowest and vice-versa

# Make changes to the data...

df['Total'] = df['HP'] + df['Attack']
print(df.head(5))


# drop the column...

df = df.drop(columns=['Total'])
print(df.head(5))

df['Total'] = df.iloc[:, 4:9].sum(axis=1)   # axis = 0 then it will add those vertically..
print(df.head(5))

cols =  list(df.columns.values)
#df = df[['Total','HP','Defense']]
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]


# Saving our data into a CV...
# to not save indexes..

df.to_csv('modified.csv', index=False)
#df.to_excel('modified.xlsx', index=False)


df.to_csv('modified.txt', index=False, sep='\t') # to seperate it with a tab or something else...

# Filtering of data...

print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])
print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')])
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 100)])

# you can then save it in a file...

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 100)]
new_df = new_df.reset_index(drop=True)
new_df = new_df.reset_index(drop=True, inplace=True)

print(new_df)

new_df = df.loc[df['Name'].str.contains('Mega')]

new_df = df.loc[~df['Name'].str.contains('Mega')]
print(new_df)   # you can use ~ tilde for negating the same...


import re

print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])  # starts with pi using regex...


# Conditional changes...
df.loc[df['Type 1'] == 'Fire', 'Type 1' ] = 'Flamer'
print(df)


df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
print(df)


df = pd.read_csv('modified.csv')
print(df.head(2))

df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['test1', 'test2']
print(df)

df = pd.read_csv('modified.csv')
print(df.head(2))

# Aggregate statics...

df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)    # you can use groupby, mean, sum , count functions... 
print(df)

df['count'] = 1
nf = df.groupby(['Type 1']).count()['count']
print(nf)


# working with larger amounts of data...
# read file in chunks..

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):     # read 5 rows at a time...
    print("CHUNF DF")
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])
    print(df)
