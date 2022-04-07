import pymysql

conn = pymysql.connect(user="root", password="admin", host="127.0.0.1", port=3305, db="python", charset="utf8")
cur = conn.cursor()

sql = "INSERT INTO emp (e_id, e_name, sex, addr) VALUES (4, 4, 4, 4)" 
data=cur.execute(sql)
print(data)
conn.commit()
    
conn.close()