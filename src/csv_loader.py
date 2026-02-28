import pandas as pd

def load_csv():
    df = pd.read_csv("data/crypto_market.csv")
    return df