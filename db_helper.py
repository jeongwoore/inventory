# db_helper.py
import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "tjwjddn0904@", 
    "database": "burger",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)
    
    def fetch_items(self):
        sql = "SELECT * FROM menu ORDER BY id"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall() 

    def insert_items(self, category, name, price, stock) :
        sql = "INSERT INTO menu (category, name, price, stock) VALUES (%s, %s, %s, %s)"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (category, name, price, stock))
                conn.commit()
                return True
            except Exception as e:
                print(e)
                conn.rollback()
                return False
    
    def update_items(self, category, id, name, price, stock) :
        sql = "UPDATE menu SET category=%s, name=%s, price=%s, stock=%s WHERE id=%s"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (category, name, price, stock, id))
                conn.commit()
                return True
            except Exception as e:
                print(e)
                conn.rollback()
                return False
    
    def delete_items(self, id) :
        sql = "DELETE FROM menu WHERE id=%s"
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (id,))
                conn.commit()
                return True
            except Exception as e:
                print(e)
                conn.rollback()
                return False