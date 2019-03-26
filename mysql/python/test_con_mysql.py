import MySQLdb

try:
    # 获取连接
    conn = MySQLdb.connect(
        host='192.168.0.103',
        user='root',
        passwd='root',
        db='news',
        port=3306,
        charset='utf8'
    )

    # 获取数据
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `news` ORDER BY `created_at` DESC;')
    rest = cursor.fetchone()
    print(rest)

    # 关闭连接
    conn.close()
except MySQLdb.Error as e:
    print(f'Error:{e}')
