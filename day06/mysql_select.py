import pymysql

# MySQL 연결
conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')
                       
# Cursor 생성
cur = conn.cursor(pymysql.cursors.DictCursor)

# SQL 실행
sql = """
        SELECT 
            e_id,
            e_name,
            gen,
            addr
        FROM 
            emp
    """
cur.execute(sql)

# 데이터 접근
result = cur.fetchall()

# 연결 종료
conn.close()

print(result)