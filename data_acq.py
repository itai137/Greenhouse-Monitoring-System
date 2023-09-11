import sqlite3
from datetime import datetime
import pandas as pd

def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, data):
    sql = ''' INSERT INTO data(timestamp, name, value)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def fetch_data(db_file, table_name, name=None):
    conn = create_connection(db_file)
    if conn is not None:
        query = f"SELECT * FROM {table_name}"
        if name:
            query += f" WHERE name = '{name}'"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    return pd.DataFrame()

def check_changes(table_name):
    conn = create_connection(db_name)
    if conn is not None:
        query = f"SELECT * FROM {table_name} WHERE last_updated = 'Y'"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    return pd.DataFrame()

if __name__ == "__main__":
    db_name = 'data/homedata_05_2.db'
    data_table = '''CREATE TABLE IF NOT EXISTS data (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        timestamp text NOT NULL,
                        name text NOT NULL,
                        value real NOT NULL
                    );'''
    create_table(create_connection(db_name), data_table)

