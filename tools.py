from analysis_tools import calculate_summary


def get_customer_count(df):
    summary = calculate_summary(df)
    return summary["unique_customers"]

def get_top_categories(df, n=10):
    summary = calculate_summary(df)
    top_categories = summary["top_product_categories"]
    return dict(list(top_categories.items())[:n])