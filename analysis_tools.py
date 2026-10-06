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

def filter_data(df, column, value):
    filtered_df = df[df[column] == value]
    return filtered_df

def calculate_summary(df):
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "data_types": df.dtypes.to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "unique_customers": df["PERSON_PUBLIC_KEY"].nunique(),
        "unique_dates": df["DATE"].nunique(),
        "channels": df["CHANNEL"].value_counts(dropna=False).to_dict(),
        "unique_product_categories": df["PRODUCT_CATEGORY"].nunique(),
        "top_product_categories": get_top_product_categories(df).to_dict(),
        "number_of_baskets": calculate_baskets(df),
    }

    basket_categories = (
        df[["PERSON_PUBLIC_KEY", "DATE", "CHANNEL", "PRODUCT_CATEGORY"]]
        .drop_duplicates()
        .groupby(["PERSON_PUBLIC_KEY", "DATE", "CHANNEL"])
        .size()
    )

    summary.update({
        "average_categories_per_basket": basket_categories.mean(),
        "min_categories_in_basket": basket_categories.min(),
        "max_categories_in_basket": basket_categories.max(),
    })

    return summary