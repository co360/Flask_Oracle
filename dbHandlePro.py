import cx_Oracle as o


def pinsertData(pname, pnum, pdate):
    try:
        # sql = "insert into st`udent values('이순신',30,'1999/02/11')"
        sql = "insert into product values(:pname,:pnum,:pdate)"
        dsn = o.makedsn('localhost', '1521', 'xe')
        conn = o.connect(user='scott', password='tiger', dsn=dsn)
        cur = conn.cursor()
        cur.execute(sql, (pname, int(pnum), pdate))
        conn.commit()
        conn.close()
        return "상품이 추가되었습니다."
    except Exception as err:
        print('err:', err)
        return "Insert Fail"


def pselectData():
    try:
        sql = "select * from product"
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
