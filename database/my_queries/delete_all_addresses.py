import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def delete_all_addresses():
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM house_addresses")
    conn.commit()
    conn.close()

#вызов функции
delete_all_addresses()