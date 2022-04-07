import pymysql

conn = pymysql.connect(user="root", password="admin", host="127.0.0.1", port=3305, db="python", charset="utf8")
cur = conn.cursor()

e_id = "4"
e_name = "1"
sex = "1"
addr = "1"

sql = f"""
UPDATE emp 
SET e_name='{e_name}', 
        sex='{sex}', 
        addr='{addr}'
WHERE e_id='{e_id}';
"""

data=cur.execute(sql)

print(data)
conn.commit()

conn.close()

