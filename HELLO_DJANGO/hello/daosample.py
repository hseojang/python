import pymysql

class DaoSmp:
    def __init__(self):
        self.conn = pymysql.connect(user="root", password="admin", host="127.0.0.1", port=3305, db="python", charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
    
        
    def myselect(self):
        sql = "SELECT * FROM sample" 
        self.curs.execute(sql) 
        rows = self.curs.fetchall()
        return rows

    def myinsert(self, col01, col02, col03):
        sql = f"""INSERT INTO sample (col01, col02, col03) VALUES ({col01}, {col02}, {col03})"""
        cnt = self.curs.execute(sql) 
        self.conn.commit()
        return cnt
    
    def myupdate(self, col01, col02, col03):
        sql = f"""UPDATE sample SET col02 = {col02}, col03 = {col03} WHERE col01 = {col01}"""
        cnt = self.curs.execute(sql) 
        self.conn.commit()
        return cnt
    
    def mydelete(self, col01):
        sql = f"""DELETE FROM sample WHERE col01={col01}"""
        cnt = self.curs.execute(sql) 
        self.conn.commit()
        return cnt

if __name__ == '__main__':
    de = DaoSmp()