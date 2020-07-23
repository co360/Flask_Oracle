import cx_Oracle as o


def insertTest(name, age, birth):
    try:
        # sql = "insert into student values('이순신',30,'1999/02/11')"
        sql = "insert into student values(:name,:age,:birth)"
        dsn = o.makedsn('localhost', '1521', 'xe')
        conn = o.connect(user='scott', password='tiger', dsn=dsn)
        cur = conn.cursor()
        cur.execute(sql, ('임꺽정', 40, '1979/03/01'))
        conn.commit()
        conn.close()
        print("oracle insert")
    except  Exception as err:
        print('err:', err)


try:
    sql = "select * from student"
    dsn = o.makedsn('localhost', '1521', 'xe')
    conn = o.connect(user='scott', password='tiger', dsn=dsn)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    for n, a, b in data:
        print(n, a, b.year, b.month, b.day)

except  Exception as err:
    print('err:', err)
