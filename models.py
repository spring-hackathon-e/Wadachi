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

    def getUserId(user_id): #user_idが登録済か判別
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

    #メッセージを全て取得
    def getMessageAll(ch_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT message_id,u.user_id,message,reaction FROM messages AS m INNER JOIN users AS u ON m.user_id WHERE ch_id = %s;"
            cursor.excecute(sql,(ch_id))
            messages = cursor.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()

    #メッセージを追加
    def addMessage(user_id,ch_id,message):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO messages(user_id,ch_id,message) VALUES (%s,%s,%s)"
            cursor.execute(sql,(user_id,ch_id,message))
            connect.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cursor.close()

    #メッセージを削除
    def deleteMessage(message_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "DELETE FROM messages WHERE message_id=%s;"
            cursor.execute(sql,(message_id))
            connect.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cursor.close()

    #リアクションの総数を収集
    def correctReaction(message_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT reaction FROM messages WHERE message_id=%s"
            cursor.excecute(sql,(message_id))
            sum_reaction = cursor.fetchone()
            return sum_reaction
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cursor.close()

    #リアクション(いいね)を追加
    def addReaction(self,message_id):
        reactions = self.correctReaction(message_id)
        reactions = reactions + 1 #いいねボタンを押されるとカウント１増やす
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "UPDATE messages SET reaction=%s WHERE message_id=%s"
            cursor.execute(sql,(reactions,message_id))
            connect.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cursor.close()