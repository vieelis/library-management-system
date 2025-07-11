import sqlite3

def connect():
    return sqlite3.connect("database/library.db")

def print_header(title):
    print("=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)