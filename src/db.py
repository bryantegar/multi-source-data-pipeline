import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "crypto.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_data (
            id TEXT,
            symbol TEXT,
            current_price REAL,
            market_cap REAL,
            sector TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_data(df):
    conn = get_connection()
    df.to_sql("crypto_data", conn, if_exists="replace", index=False)
    conn.close()