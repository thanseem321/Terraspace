
import sqlite3

DATABASE = "terraspace.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            target TEXT NOT NULL,
            extraterrestrial_match TEXT,
            latitude REAL,
            longitude REAL,
            terrain TEXT,
            similarity_score TEXT,
            traits TEXT,
            testing TEXT,
            nasa_dataset TEXT,
            nasa_url TEXT
        )
    """)

    conn.commit()
    conn.close()
