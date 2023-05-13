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
        # エラー処理
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
