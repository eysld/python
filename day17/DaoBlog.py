import pymysql
class DaoBlog:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305,
                           user='root', password='python',
                           db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    
    def insert(self, title, link, description, bloggername, bloggerlink, postdate):
        sql = """
            INSERT INTO blog 
                (title, link, description, bloggername, bloggerlink, postdate) 
            VALUES 
            (%s, %s, %s, %s, %s, %s)
        """
        
        cnt = self.cur.execute(sql, (title, link, description, bloggername, bloggerlink, postdate))
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == "__main__":
    db = DaoBlog()
