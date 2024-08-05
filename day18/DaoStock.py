import pymysql

class DaoStock:
    def __init__(self):
        self.con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python',
                               db='python', charset='utf8')
                               
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    
    def insert(self,s_code,s_name,price,ymd):
        query = f"""
            INSERT INTO stock 
                (s_code,s_name,price,ymd) 
            VALUES 
                ("{s_code}","{s_name}","{price}","{ymd}")
        """
        
        
        cnt = self.cur.execute(query)
        self.con.commit()
        return cnt
        
        
    def __del__(self):
        self.cur.close()
        self.con.close()
        
if __name__ == '__main__':
    ds = DaoStock()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    