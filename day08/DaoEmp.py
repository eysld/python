import pymysql
class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305,
                           user='root', password='python',
                           db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    
    def selectList(self):
        sql = """
            SELECT 
            e_id,
            e_name,
            gen,
            addr
        FROM 
            emp
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    def select(self, e_id):
        sql = f"""
            SELECT 
            e_id,
            e_name,
            gen,
            addr
        FROM 
            emp
        WHERE 
            e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return vo
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
            INSERT INTO emp 
                (e_id, e_name, gen, addr) 
            VALUES 
            ({e_id}, '{e_name}', '{gen}', '{addr}')
        """
        
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        sql = f"""
            UPDATE emp
            SET
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            where
                e_id = {e_id}
        """
        
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            delete from emp
            where 
                e_id = {e_id}
        """
        
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt   
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == "__main__":
    de = DaoEmp()
    list = de.selectList()
    vo = de.select('1')
    cnt = de.delete(3)
    print(cnt)