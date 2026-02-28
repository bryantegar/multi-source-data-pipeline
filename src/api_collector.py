import requests
import json

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

def fetch_api_data():
    response = requests.get(URL)
    data = response.json()

    with open("data/crypto_api.json", "w") as f:
        json.dump(data, f, indent=2)

    print("API data saved")

if __name__ == "__main__":
    fetch_api_data()