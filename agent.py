import pandas as pd
from analysis_tools import count_filtered_rows, calculate_summary

df = pd.read_csv("Data/transactions_part_01.csv")

question = input("Please enter your question: ")

if "online" in question.lower():
    result = count_filtered_rows(df, "CHANNEL", "ONLINE")
    print(f"There are {result} online transactions.")
elif "offline" in question.lower():
    result = count_filtered_rows(df, "CHANNEL", "OFFLINE")
    print(f"There are {result} offline transactions.")
elif "customers" in question.lower():
    summary = calculate_summary(df)
    print(f"There are {summary['unique_customers']} customers in the dataset.")