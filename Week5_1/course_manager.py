from database import create_connection
import sqlite3

def add_course(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def search_course(id,name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course WHERE name LIKE ? and id  = ?", ('%' + name + '%', id))
    rows = cursor.fetchall()
    conn.close()
    return rows
