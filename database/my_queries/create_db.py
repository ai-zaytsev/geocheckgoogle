import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_database():
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    # Подключение к базе данных (или ее создание, если она не существует)
    conn = sqlite3.connect(db_path)

    # Создание таблицы
    conn.execute('''CREATE TABLE IF NOT EXISTS house_addresses (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       address TEXT NOT NULL
                   )''')

    # Закрытие соединения с базой данных
    conn.close()

create_database()