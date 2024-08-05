import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')



sql = """
    UPDATE emp 
    SET 
        e_name = %s 
    WHERE e_id = %s
    """
val = ("가나다", "3")

with conn:
    with conn.cursor() as cur:
        cur.execute(sql, val)
        conn.commit()