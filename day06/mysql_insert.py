import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3305,
                       user='root', password='python',
                       db='python', charset='utf8')

# try:
#     curs = conn.cursor()
#     sql = "INSERT INTO emp (e_id, e_name, gen, addr) VALUES (%s, %s, %s, %s)"
#     val = (3, "3", "3", "3")
#     cnt = curs.execute(sql, val)
#     print(cnt)
#     conn.commit()
#
# finally:
#     conn.close()

cur = conn.cursor()
e_id = 3
e_name = "3"
addr = "3"
gen = "3"

sql = f"""
    INSERT INTO emp 
        (e_id, e_name, gen, addr) 
    VALUES 
    ({e_id}, '{e_name}', '{gen}', '{addr}')
    """
cnt = cur.execute(sql)
print(cnt)

conn.commit()
cur.close()
conn.close()