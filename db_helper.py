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
    def __init__(self, host=None, user=None, password=None, database=None, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor):
        self.connection = None
        self.config = {
            "host": host or DB_CONFIG["host"],
            "user": user or DB_CONFIG["user"],
            "password": password or DB_CONFIG["password"],
            "database": database or DB_CONFIG["database"],
            "charset": charset,
            "cursorclass": cursorclass
        }

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(**self.config)
        return self.connection

    def fetchall(self, query, params=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"조회 에러: {e}")
            return []
