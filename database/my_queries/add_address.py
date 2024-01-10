import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def add_specific_address(address):
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO house_addresses (address) VALUES (?)", (address,))
    conn.commit()
    conn.close()

# Вызов функции для добавления адреса
add_specific_address("")