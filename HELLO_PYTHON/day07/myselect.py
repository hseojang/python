import pymysql
import mariadb

conn = pymysql.connect(user="root", password="admin", host="127.0.0.1", port=3305, db="python", charset="utf8")
cursor = conn.cursor()

sql = "SELECT e_id, e_name, sex, addr FROM emp" 

cursor.execute(sql) 

result = cursor.fetchall()

print(result)

conn.commit
conn.close()