import sqlite3

DB_PATH = "shop.db"


def run_query(table, username):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM {table} WHERE username = '{username}'"
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows
