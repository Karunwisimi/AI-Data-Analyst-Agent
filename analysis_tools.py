import pandas as pd

def calculate_baskets(df):
    baskets = (
        df[["PERSON_PUBLIC_KEY", "DATE", "CHANNEL"]]
        .drop_duplicates()
        .shape[0]
    )

    return baskets