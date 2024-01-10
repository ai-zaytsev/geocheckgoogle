import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_all_addresses():
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT address FROM house_addresses")
    addresses = cursor.fetchall()
    conn.close()
    return addresses

# Получение и вывод всех адресов
all_addresses = get_all_addresses()
for address in all_addresses:
    print(address[0])  # Вывод каждого адреса