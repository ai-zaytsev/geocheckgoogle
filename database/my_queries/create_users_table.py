import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_users_table():
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY
                    )''')
    conn.close()

create_users_table()