import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(user="root", password="admin", host="127.0.0.1", port=3305, db="python", charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
    
        
    def myselect(self):
        sql = "SELECT * FROM emp" 
        self.curs.execute(sql) 
        rows = self.curs.fetchall()
        return rows

    def myinsert(self, e_id, e_name, sex, addr):
        sql = f"""INSERT INTO emp (e_id, e_name, sex, addr) VALUES ({e_id}, {e_name}, {sex}, {addr})"""
        cnt = self.curs.execute(sql) 
        self.conn.commit()
        return cnt
    
    def myupdate(self, e_id, e_name, sex, addr):
        sql = f"""UPDATE emp SET e_name = {e_name}, sex = {sex}, addr = {addr} WHERE e_id = {e_id}"""
        cnt = self.curs.execute(sql) 
        self.conn.commit()
        return cnt
    
    def mydelete(self, e_id):
        sql = f"""DELETE FROM emp WHERE e_id={e_id}"""
        cnt = self.curs.execute(sql) 
        self.conn.commit()
        return cnt

if __name__ == '__main__':
    de = DaoEmp()
    rslt = de.mydelete(5)
    print(rslt)