import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_all_clicks():
    db_path = os.path.join(BASE_DIR, "../addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT click_count FROM button_clicks")
    clicks = cursor.fetchall()
    conn.close()
    return clicks

print(get_all_clicks())