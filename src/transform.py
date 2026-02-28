import pandas as pd
import json

def transform_api():
    with open("data/crypto_api.json") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df = df[["id","symbol","current_price","market_cap"]]
    return df