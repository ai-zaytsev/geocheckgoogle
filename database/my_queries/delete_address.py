import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def delete_specific_address(address):
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM house_addresses WHERE id = ?", (address,))
    conn.commit()
    conn.close()

# Вызов функции для добавления адреса
delete_specific_address("")