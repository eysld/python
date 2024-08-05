import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')

sql = "delete from emp  WHERE e_id = %s"
val =  3

with conn:
    with conn.cursor() as cur:
        cur.execute(sql, val)
        conn.commit()