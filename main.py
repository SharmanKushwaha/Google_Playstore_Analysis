import numpy as np
import pandas as pd
print("=" * 60)
print("GOOGLE PLAYSTORE ANALYSIS")
print("=" * 60)
df = pd.read_csv('data/googleplaystore.csv') 
print("Dataset loaded successfully!")
# print(df.head())
# print(df.info())
# print(df['Installs'].unique())
# print(df['Price'].unique())
# print(df['Size'].unique())
# print(df['Type'].unique())
# s1 = pd.Series(df['Size'].unique())
# print(s1)
# print(df['Size'].unique().tolist())
# Find rows where 'Installs' is not numeric
df['Installs'] = df['Installs'].replace('Free', '0')
mask = df['Installs'].str.isnumeric() == False
print(df[mask][['App', 'Installs', 'Type']])
df['Installs'] = df["Installs"].str.replace('+','', regex=False)
df['Installs'] = df["Installs"].str.replace(',','', regex=False)
df['Installs'] = df['Installs'].astype(int)
# print(df[['App', 'Installs']].head())
# print(df['Installs'].describe())
print(f"Max installs: {df['Installs'].max():,}")
print(f"Min installs: {df['Installs'].min():,}")
# Count rows where Installs is exactly 0
zero_count = (df['Installs'] == 0).sum()
print(f"Number of apps with 0 installs: {zero_count}")
# Installs column cleaned successfully!
bad_price_rows = df[~df['Price'].str.replace('$', '', regex=False).str.isnumeric()]
print(f"Rows with non-numeric Price: {len(bad_price_rows)}")
print(bad_price_rows[['App', 'Price', 'Type']])
df['Price'] = df['Price'].str.replace('$','',regex=False)
df['Price'] = df['Price'].replace('Everyone', '0')
df['Price'] = df['Price'].astype(float)
print(df['Price'].head(10))
print(df['Price'].describe())