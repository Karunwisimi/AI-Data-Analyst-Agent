## First inspection

import pandas as pd
from analysis_tools import (
    calculate_baskets,
    get_top_product_categories,
    filter_data,
    calculate_summary
)

file_path = "Data/transactions_part_01.csv"

df = pd.read_csv(file_path)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nUnique customers:")
print(df["PERSON_PUBLIC_KEY"].nunique())

print("\nUnique dates:")
print(df["DATE"].nunique())

print("\nChannels:")
print(df["CHANNEL"].value_counts(dropna=False))

print("\nUnique product categories:")
print(df["PRODUCT_CATEGORY"].nunique())

print("\nTop 10 product categories:")
print(get_top_product_categories(df))

# # Let's investigate the baskets
print("\nNumber of baskets:")
print(calculate_baskets(df))

basket_categories = (
    df[["PERSON_PUBLIC_KEY", "DATE", "CHANNEL", "PRODUCT_CATEGORY"]]
    .drop_duplicates()
    .groupby(["PERSON_PUBLIC_KEY", "DATE", "CHANNEL"])
    .size()
)

print("\nAverage categories per basket:")
print(basket_categories.mean())

print("\nMinimum categories in a basket:")
print(basket_categories.min())

print("\nMaximum categories in a basket:")
print(basket_categories.max())

print("\nONLINE transactions:")
print(filter_data(df, "CHANNEL", "ONLINE").head())

print("\nDataset summary:")
print(calculate_summary(df))