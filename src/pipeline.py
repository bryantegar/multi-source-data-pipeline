from src.api_collector import fetch_api_data
from src.csv_loader import load_csv
from src.transform import transform_api
from src.merge import merge_data
from src.validate import validate
from src.logger import logger
from src.db import create_table, insert_data
from src.validate import validate, remove_duplicates

import pandas as pd

def run_pipeline():
    logger.info("Pipeline started")

    df_api = transform_api()
    df_csv = load_csv()

    merged = merge_data(df_api, df_csv)
    logger.info(f"Merged dataset size: {len(merged)}")

    validate(merged)
    logger.info("Validation passed")

    create_table()
    insert_data(merged)
    logger.info("Data stored in SQLite database")

    merged.to_csv("output/final_dataset.csv", index=False)

    logger.info("Pipeline success")
    print("Pipeline success")

    logger.info(f"Columns: {list(merged.columns)}")
    logger.info(f"Average price: {merged['current_price'].mean()}")

if __name__ == "__main__":
    run_pipeline()