import pymysql
class DaoQuestion:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305,
                           user='root', password='python',
                           db='python', charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = """
            SELECT
                q_num,
                que,
                ans1,
                ans2,
                ans3,
                ans4,
                ans
            from 
                question
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    # def select(self, q_num):
    #      sql = f"""
    #         SELECT
    #             q_num,
    #             que,
    #             ans1,
    #             ans2,
    #             ans3,
    #             ans4,
    #             ans
    #         from 
    #             question
    #         where
    #             q_num = '{q_num}'
    #     """
    #     self.cur.execute(sql)
    #     vo = self.cur.fetchone()
    #     return vo
    #
    # def insert(self, q_num, que, ans1, ans2, ans3, ans4,ans):
    #     sql = f"""
    #         INSERT INTO question
    #             (q_num,que, ans1, ans2, ans3, ans4, ans)
    #         VALUES
    #         ({q_num}, '{que}', '{ans1}', '{ans2}', '{ans3}', '{ans4}', '{ans}')
    #     """    
            
if __name__ == "__main__":
    dq = DaoQuestion()
    list = dq.selectList()
    print(list)