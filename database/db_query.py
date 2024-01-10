import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def address_exists(address):
    db_path = os.path.join(BASE_DIR, "addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM house_addresses WHERE address = ?", (address,))
    record = cursor.fetchone()
    conn.close()
    return record

def add_address(address):
    if not address_exists(address):
        db_path = os.path.join(BASE_DIR, "addresses.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO house_addresses (address) VALUES (?)", (address,))
        conn.commit()
        conn.close()
    return False
