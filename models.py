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

    def getChannelAll():# チャンネル一覧機能
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels;"
            cursor.execute(sql)
            channels = cursor.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()


    def getChannelById(ch_id):# チャンネル作成機能
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cursor.execute(sql, (ch_id))
            channel = cursor.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()


    def getChannelByName(ch_name):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cursor.execute(sql, (ch_name))
            channel = cursor.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()


    def addChannel(user_id, newCh_Name, newChannel_summary):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO channels (user_id, name, abstract) VALUES (%s, %s, %s);"
            cursor.execute(sql, (user_id, newCh_Name, newChannel_summary))
            connect.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()


    def getChannelByName(ch_name):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cursor.execute(sql, (ch_name))
            channel = cursor.fetchone()
        except Exception as e:
            print(e + 'が発生しました')
            return None
        finally:
            cursor.close()
            return channel


    def updateChannel(user_id, newCh_Name, newChannel_summary, ch_id): # チャンネル編集機能
        connect = DB.getConnection()
        cursor = connect.cursor()
        sql = "UPDATE channels SET user_id=%s, name=%s, abstract=%s WHERE id=%s;"
        cursor.execute(sql, (user_id, newCh_Name, newChannel_summary, ch_id))
        connect.commit()
        cursor.close()

    def deleteChannel(ch_id): # チャンネル削除機能
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cursor.execute(sql, (ch_id))
            connect.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()

