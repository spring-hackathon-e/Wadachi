import pymysql

class DB:
    def getConnection():
        #例外処理
        try:
            conn = pymysql.connect(
                host="localhost",
                db="Wadachi",
                user="gruper",
                password="spring_e",
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor
            )
            return conn
        #エラー処理
        except(ConnectionError):
            print("コネクションエラーです")
            conn.close()