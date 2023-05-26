import pymysql

class DB:
    def getConnection():
        # 例外処理
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
        # エラー表示
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
