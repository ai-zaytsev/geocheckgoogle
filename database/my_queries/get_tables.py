import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_all_tables():
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]  # Возвращает список названий таблиц

# Вывод всех таблиц
print(get_all_tables())