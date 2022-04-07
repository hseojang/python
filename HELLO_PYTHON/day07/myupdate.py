import pymysql

conn = pymysql.connect(user="root", password="admin", host="127.0.0.1", port=3305, db="python", charset="utf8")
cur = conn.cursor()

# sql = "UPDATE emp SET e_name=5, sex=5, addr=6 WHERE e_id=4" 
sql = "UPDATE emp SET e_name=%s, sex=%s, addr=%s WHERE e_id=%s" 
data=cur.execute(sql, ('5', '5', '5', '4'))
# 순서대로 들어감 반환하는 값은 실행된 쿼리의 수 

print(data)
conn.commit()
    
conn.close()