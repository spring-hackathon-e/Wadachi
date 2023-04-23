import pymysql
from util.DB import DB

class dbConnect:
    def createUser(user): ##ユーザ情報追加
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO users (user_id, user_name, email, user.password) VALUES (%s,%s,%s,%s);"
            cursor.execute(sql, (user.user_id, user.user_name, user.email, user.password))
            connect.commit()
        except Exception as e:
            print(e + 'が発生しています。')
            return None
        finally:
            cursor.close()

    def getUser(email): #emailが登録済みか判別
        try: 
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT email FROM users WHERE email=%s" ##app.pyでgetしたemail
            cursor.execute(sql, (email,))
            reg_email = cursor.fetchone()
            return reg_email ##登録済みのemailを返す。なければNoneを返す。
        except Exception as e: ##エラーの見える化
            print(e + 'が発生しています。')
            return None
        finally:
            cursor.close()

    def getUserId(user_id):　#user_idが登録済か判別
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT user_id FROM users WHERE user_id=%s"
            cursor.execute(sql, (user_id,))
            reg_user_id = cursor.fetchone()
            return reg_user_id
        except Exception as e: ##エラーの見える化
            print(e + 'が発生しています。')
            return None
        finally:
            cursor.close()
