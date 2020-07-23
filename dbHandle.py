import cx_Oracle as o


def insertData(name, age, birth):
    try:
        # sql = "insert into st`udent values('이순신',30,'1999/02/11')"
        sql = "insert into student values(:name,:age,:birth)"
        dsn = o.makedsn('localhost', '1521', 'xe')
        conn = o.connect(user='scott', password='tiger', dsn=dsn)
        cur = conn.cursor()
        cur.execute(sql, (name, int(age), birth))
        conn.commit()
        conn.close()
        return "Oracle Insert"
    except Exception as err:
        print('err:', err)
        return "Insert Fail"


def selectData():
    try:
        sql = "select * from student"
        dsn = o.makedsn('localhost', '1521', 'xe')
        conn = o.connect(user='scott', password='tiger', dsn=dsn)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        conn.close()
        return data
    except Exception as err:
        print('err:', err)
        return None
