import time
from src.pipeline import run_pipeline

while True:
    run_pipeline()
    print("Waiting 60 seconds...")
    time.sleep(60)