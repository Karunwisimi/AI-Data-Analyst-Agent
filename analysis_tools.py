import pandas as pd

def calculate_baskets(df):
    baskets = (
        df[["PERSON_PUBLIC_KEY", "DATE", "CHANNEL"]]
        .drop_duplicates()
        .shape[0]
    )

    return baskets

def get_top_product_categories(df, n=10):
    top_categories = df["PRODUCT_CATEGORY"].value_counts().head(n)
    return top_categories