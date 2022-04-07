e_id = "1"
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
# 파이썬 3.5 이후부터 지원하는 내용 

print(sql)
