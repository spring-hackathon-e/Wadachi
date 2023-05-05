import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
                host="localhost",
                db="Wadachi",
                user="gruper",
                password="Spring_e6",
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor
            )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
