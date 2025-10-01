import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="tjwjddn0904@",
    database="burger",
    charset="utf8"
)

cur = conn.cursor()


cur.execute("SELECT VERSION()")


result = cur.fetchone()
print("Database version:", result)


cur.close()
conn.close()