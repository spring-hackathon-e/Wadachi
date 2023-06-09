import pymysql
import datetime
from util.DB import DB


class dbConnect:
    # ユーザー情報追加
    def createUser(user):
        goal = ""
        start_date = "2022/04/12"
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO users (user_id, user_name, email, password,goal,start_date) VALUES (%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, (user.user_id, user.user_name,user.email, user.password,goal,start_date))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # emailが登録済みか判別
    def getUser(email):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cursor.execute(sql, (email))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    def getUserById(user_id):
            try:
                connect = DB.getConnection()
                cursor = connect.cursor()
                sql = "SELECT * FROM users WHERE user_id=%s;"
                cursor.execute(sql, (user_id))
                user = cursor.fetchone()
                return user
            except Exception as e:
                print(str(e) + 'が発生しています。')
                return None
            finally:
                cursor.close()

    # user_idが登録済か判別
    def getUserId(user_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT user_id FROM users WHERE user_id=%s;"
            cursor.execute(sql, (user_id,))
            reg_user_id = cursor.fetchone()
            return reg_user_id
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    def getUserById(user_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM users WHERE user_id=%s;"
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    #パスワードリセット
    def reset_password(email, password):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "UPDATE users SET password = %s WHERE email = %s;"
            cursor.execute(sql, (password, email))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()


    # メッセージを全て取得
    def getMessageAll(ch_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT message_id,u.user_id,user_name,message,reaction FROM messages AS m INNER JOIN users AS u ON m.user_id = u.user_id WHERE ch_id = %s;"
            cursor.execute(sql, (ch_id))
            messages = cursor.fetchall()
            return messages
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # メッセージを追加
    def addMessage(user_id, ch_id, message,reaction):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO messages(user_id,ch_id,message,reaction) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (user_id, ch_id, message,reaction))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # メッセージを削除
    def deleteMessage(message_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "DELETE FROM messages WHERE message_id=%s;"
            cursor.execute(sql, (message_id))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # リアクションの総数を収集
    def correctMeReaction(message_id): #Me = Message
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT reaction FROM messages WHERE message_id=%s;"
            cursor.excecute(sql, (message_id))
            sum_reaction = cursor.fetchone()
            return sum_reaction
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # リアクション(いいね)を追加
    def addMeReaction(self, message_id):
        reactions = self.correctMeReaction(message_id)
        reactions = reactions + 1  # いいねボタンを押されるとカウント１増やす
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "UPDATE messages SET reaction=%s WHERE message_id=%s;"
            cursor.execute(sql, (reactions, message_id))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # チャンネル一覧機能
    def getChannelAll():
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels;"
            cursor.execute(sql)
            channels = cursor.fetchall()
            return channels
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # チャンネル作成(ch_id)
    def getChannelById(ch_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels WHERE ch_id=%s;"
            cursor.execute(sql, (ch_id))
            channel = cursor.fetchone()
            return channel
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # チャンネル作成(ch_name)
    def getChannelByName(ch_name):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT * FROM channels WHERE ch_name=%s;"
            cursor.execute(sql, (ch_name))
            channel = cursor.fetchone()
            return channel
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # チャンネル作成(user_id, Ch_Name, Channel_summary, main_category, sub_category)
    def addChannel(user_id, newCh_Name, newChannel_summary,main,sub):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO channels (user_id, ch_name, summary,main_category,sub_category) VALUES (%s, %s, %s,%s, %s);"
            cursor.execute(sql, (user_id, newCh_Name, newChannel_summary,main,sub))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # チャンネル編集機能
    def updateChannel(user_id, newCh_Name, newChannel_summary,ch_id):
        connect = DB.getConnection()
        cursor = connect.cursor()
        sql = "UPDATE channels SET user_id=%s, ch_name=%s, summary=%s WHERE ch_id=%s;"
        cursor.execute(sql, (user_id, newCh_Name, newChannel_summary, ch_id))
        connect.commit()
        cursor.close()

    # チャンネル削除機能
    def deleteChannel(ch_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "DELETE FROM channels WHERE ch_id=%s;"
            cursor.execute(sql, (ch_id))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    #全ての勉強記録を取得
    def getPostAll():
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT post_id,post,u.user_id,user_name,goal,study_time FROM posts AS p INNER JOIN users AS u ON p.user_id = u.user_id;"
            cursor.execute(sql)
            posts= cursor.fetchall()
            return posts
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    #勉強記録の追加
    def addPost(user_id, post, study_time):
        title = 'こんにちは'
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "INSERT INTO posts(user_id, title, post, study_time) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (user_id, title, post, study_time))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    #勉強記録の削除
    def deletePost(post_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "DELETE FROM posts WHERE post_id=%s;"
            cursor.execute(sql, (post_id))
            connect.commit()
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # リアクションの総数を収集
    def correctPoReaction(post_id): #Po = post
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "SELECT reaction FROM posts WHERE post_id=%s"
            cursor.excecute(sql, (post_id))
            sum_reaction = cursor.fetchone()
            return sum_reaction
        except Exception as e:
            print(str(e) + 'が発生しています。')
            return None
        finally:
            cursor.close()

    # リアクション(いいね)を追加
    def addPoReaction(self, post_id):
        reactions = self.correctPoReaction(post_id)
        reactions = reactions + 1  # いいねボタンを押されるとカウント１増やす
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "UPDATE posts SET reaction=%s WHERE post_id=%s"
            cursor.execute(sql, (reactions, post_id))
            connect.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cursor.close()

    # 目標設定の編集
    def updateGoal(goal,deadline,user_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "UPDATE users SET goal=%s,deadline=%s WHERE user_id=%s;"
            cursor.execute(sql, (goal,deadline,user_id))
            connect.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cursor.close()

    # ユーザ削除
    def deleteUser(user_id):
        try:
            connect = DB.getConnection()
            cursor = connect.cursor()
            sql = "DELETE FROM users WHERE user_id=%s;"
            cursor.execute(sql, (user_id))
            connect.commit()
        except Exception as e:
            print(e + "が発生しています")
            return None
        finally:
            cursor.close()