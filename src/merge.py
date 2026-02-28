import pandas as pd

def merge_data(df_api, df_csv):
    merged = pd.merge(df_api, df_csv, on="symbol", how="inner")
    return merged