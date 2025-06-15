import sqlite3
import os

def create_connection():
    db_path = os.path.abspath("/Users/sunwenpei/swp/week1/Week5_1/users.db")
    conn = sqlite3.connect(db_path)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
