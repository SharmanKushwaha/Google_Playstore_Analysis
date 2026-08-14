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
# print(df[mask][['App', 'Installs', 'Type']])
df['Installs'] = df["Installs"].str.replace('+','', regex=False)
df['Installs'] = df["Installs"].str.replace(',','', regex=False)
df['Installs'] = df['Installs'].astype(int)
# print(df[['App', 'Installs']].head())
# print(df['Installs'].describe())
# print(f"Max installs: {df['Installs'].max():,}")
# print(f"Min installs: {df['Installs'].min():,}")
# Count rows where Installs is exactly 0
zero_count = (df['Installs'] == 0).sum()
# print(f"Number of apps with 0 installs: {zero_count}")
# Installs column cleaned successfully!
bad_price_rows = df[~df['Price'].str.replace('$', '', regex=False).str.isnumeric()]
# print(f"Rows with non-numeric Price: {len(bad_price_rows)}")
# print(bad_price_rows[['App', 'Price', 'Type']])
df['Price'] = df['Price'].str.replace('$','',regex=False)
df['Price'] = df['Price'].replace('Everyone', '0')
df['Price'] = df['Price'].astype(float)
# print(df['Price'].head(10))
# print(df['Price'].describe())
# print(df['Size'].unique().tolist())
df.loc[df['Size'] == 'Varies with device', 'Size'] = np.nan
# Find rows where 'Size' contains a value that looks like an install number (has '+')
misaligned_mask = df['Size'].str.contains(r'\+', na=False)
# print(f"Rows with misaligned data: {misaligned_mask.sum()}")
# print(df[misaligned_mask][['App', 'Size', 'Installs', 'Price']].head(10))
df = df[~misaligned_mask]
# Verify it's gone
# print(f"Remaining rows: {len(df)}")
df['Size_MB'] = (
    df['Size']
    .str.replace('k','', regex=False)
    .str.replace('M','', regex=False)
    .astype(float)
)
df['Size_MB'] = np.where(
    df['Size'].str.contains('k', na=False),
    df['Size_MB']/1024,
    df['Size_MB']
)
# print(df[['Size', 'Size_MB']].tail(10))
# Cleared Size column
# print(df['Reviews'].head(15))
# print(df['Reviews'].to_list())
df['Reviews'] = pd.to_numeric(df['Reviews'])
# print(df['Reviews'].dtype)
# Reviews column cleaned
# print(df['Rating'].to_list())
# print(f"Missing rating before: {df['Rating'].isnull().sum()}")
df['Rating'] = df['Rating'].fillna(0)
# print(f"Missing ratings after: {df['Rating'].isnull().sum()}")
# print(df['Rating'].describe())
# Cleaned Rating column
# print(df['Last Updated'].to_list())
df['Last Updated'] = pd.to_datetime(df['Last Updated'])
# print(df['Last Updated'].head(10))
# print(df['Last Updated'].isnull().sum())
bad_dates = df[df['Last Updated'].isnull()]
# print(df['Last Updated'].head())
# Last Updated column cleaned
# print(df['Type'].unique())
# print(df['Type'].isnull().sum())
# print(df['Type'].value_counts())
df['Type'] = df['Type'].fillna('Free')
# print(df['Type'].value_counts())
# Type column cleaned
# print(df['Content Rating'].unique())
# print(df['Content Rating'].isnull().sum())
# Content Rating Already Cleaned
# Checking for Duplicates
print(df['App'].duplicated().sum())
rows_before = len(df)
duplicate_count = df['App'].duplicated().sum()
print(f"Rows before: {rows_before}")
print(f"Duplicate rows: {duplicate_count}")
df = df.drop_duplicates(subset=['App'], keep='first')
rows_after = len(df)
removed = rows_before - rows_after
# print(f"Rows after: {rows_after}")
# print(f"Removed: {removed} rows")
print("\n" + "=" * 60)
print("ANALYSIS & INSIGHTS")
print("=" * 60)
# Q1: Which categories have the most apps?
top_categories = df['Category'].value_counts().head(10)
print("\n1. Top 10 categories by app count: ")
print(top_categories)
# Q2: Which category have the most installs?
category_installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)
print("\n2. Top 10 categories by total installs: ")
print(category_installs)
# Q3: Are  paid apps rated higher than the free apps?
Avg_rating = df.groupby('Type')['Rating'].mean()
print("\n3. Comparison of rating between free and paid apps: ")
print(Avg_rating)
# Q4: What is the avg price of paid apps?
paid_apps = df[df['Type'] == 'Paid']
avg_price = paid_apps['Price'].mean()
print(avg_price)
# Q5: Which apps have the highest number of reviews?
top_reviwed_apps = df.nlargest(10, 'Reviews')[['App', 'Reviews', 'Category']]
print("\n5. Top 10 apps with the most reviews: ")
print(top_reviwed_apps)
# Q6: Which apps have the highest number of installs?
top_installed_apps = df.nlargest(10, 'Installs')[['App', 'Installs', 'Category']]
print("\n6. Top 10 apps with the most installs: ")
print(top_installed_apps)
# Q7: Which category has the highest average rating?
avg_rating_by_category = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head()
print("\n7. Top 5 categories by average rating:")
print(avg_rating_by_category)
# Q8: Which category has the highest average installs?
avg_installs_by_category = df.groupby('Category')['Installs'].mean().sort_values(ascending=False).head()
print("\n8. Top 5 categories by average installs:")
for category, avg_installs in avg_installs_by_category.items():
    print(f"{category}: {avg_installs:,.0f}")
app_count_by_type = df['Type'].value_counts()
print("\n9. Free vs Paid apps:")
print(app_count_by_type)
# Q10: What is the average rating of free vs paid apps?
avg_rating_free_paid = df.groupby('Type')['Rating'].mean()
print("\n10. Average rating of free vs paid apps:")
print(avg_rating_free_paid)