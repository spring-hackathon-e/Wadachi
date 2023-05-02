import pymysql
from util.DB import DB


class dbConnect:
    def createUser(user):   # ユーザ情報追加
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO users (user_id, user_name, email, user.password) VALUES (%s,%s,%s,%s);"
            cursor.execute(sql, (user.user_id, user.user_name,
                           user.email, user.password))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    def getUserId(email):   # emailが登録済みか判別
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT user_id FROM users WHERE email=%s"   # app.pyでgetしたemail
            cursor.execute(sql, (email,))
            id = cursor.fetchone()
            return id   # 登録済みのemailを返す。無ければNone
        except Exception as e:   # エラーの見える化
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close

    def getUser(email):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM users WHERE email=%s"
            cursor.execute(sql, (email,))
            user = cursor.fetchone()
            return user
        except Exception as e:   # エラーの見える化
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close
