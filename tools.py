
from analysis_tools import calculate_summary, count_filtered_rows


def get_customer_count(df):
    summary = calculate_summary(df)
    return summary["unique_customers"]


def get_top_categories(df, n=10):
    summary = calculate_summary(df)
    top_categories = summary["top_product_categories"]
    return dict(list(top_categories.items())[:n])


def get_channel_count(df, channel):
    return count_filtered_rows(df, "CHANNEL", channel.upper())