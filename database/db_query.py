import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def address_exists(address):
    db_path = os.path.join(BASE_DIR, "addresses.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS house_addresses (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       address TEXT NOT NULL
                   )''')
    cursor.execute("SELECT * FROM house_addresses WHERE address = ?", (address,))
    record = cursor.fetchone()
    conn.close()
    return record

def add_address(address):
    if not address_exists(address):
        db_path = os.path.join(BASE_DIR, "addresses.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS house_addresses (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       address TEXT NOT NULL
                   )''')
        cursor.execute("INSERT INTO house_addresses (address) VALUES (?)", (address,))
        conn.commit()
        conn.close()
    return False

def add_user(user_id):
    db_path = os.path.join(BASE_DIR, "addresses.db")
    conn = sqlite3.connect(db_path) 
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)''')
    cursor.execute('''SELECT user_id FROM users WHERE user_id = ?''', (user_id,))
    if cursor.fetchone() is None:
        cursor.execute('''INSERT INTO users (user_id) VALUES (?)''', (user_id,))
        conn.commit()
    conn.close()

def increment_button_click_count(button_id):
    db_path = os.path.join(BASE_DIR, "addresses.db")
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS button_clicks (button_id TEXT PRIMARY KEY, click_count INTEGER DEFAULT 0)''')
    cursor.execute('''SELECT click_count FROM button_clicks WHERE button_id = ?''', (button_id,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('''INSERT INTO button_clicks (button_id, click_count) VALUES (?, 1)''', (button_id,))
    else:
        click_count = row[0] + 1
        cursor.execute('''UPDATE button_clicks SET click_count = ? WHERE button_id = ?''', (click_count, button_id))
    conn.commit()
    conn.close()