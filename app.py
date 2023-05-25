from flask import Flask, request, redirect, render_template, session, flash
from models import dbConnect
from util.user import User
from datetime import timedelta
from itsdangerous.url_safe import URLSafeTimedSerializer  # リマインド機能
from datetime import datetime
import hashlib
import uuid
import re

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)


# サインアップ
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')


@app.route('/signup', methods=['POST'])
def usersignup():   # 登録情報の取得
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password1')
    password_chk = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if user_name == '' or email == '' or password == '' or password_chk == '':
        flash('空のフォームがあります')
    elif password != password_chk:
        flash('パスワードが一致していません。')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスを記入してください。')
    else:
        user_id = uuid.uuid4
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = User(user_id, user_name, email, password)
        DbUser = dbConnect.getUser(email)

        if DbUser != None:   # emailが登録済み
            flash('すでに登録済みのユーザーです。')
        else:
            dbConnect.createUser(user)
            UserId = str(user_id)
            session['user_id'] = UserId
            user = dbConnect.getUser(email)
            return render_template('index.html', user=user)
    return redirect('/signup')   # 入力情報のクリア


# ログイン
@app.route('/login')
def login():
    return render_template('registration/login.html')


@app.route('/login', methods=['POST'])
def userlogin():  # user_idとemailを格納先と照合
    email = request.form.get('email')
    password = request.form.get('password')

    user = dbConnect.getUser(email)

    if user == None:
        flash('ユーザーIDが間違っています。')
    else:
        hashpassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if hashpassword != user["password"]:
            flash('パスワードが間違っています。')
        else:
            session['user_id'] = user["user_id"]
            return render_template('index.html', user=user)
    return redirect('/login')


# ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# メッセージ追加
app.route('/message', methods=['POST'])


def add_message():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    message = request.form.get('message')
    ch_id = request.form.get('channel_id')
    reaction = 0  # reaction数の初期値:0

    if message:
        dbConnect.addMessamge(user_id, ch_id, message, reaction)

    channel = dbConnect.getChannelById(ch_id)
    messages = dbConnect.getMessageAll(ch_id)

    return render_template('detail.html', messages=messages, channel=channel, user_id=user_id)


# メッセージ削除
app.route('/delete_message', methods=['POST'])


def delete_message():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    ch_id = request.form.get('channel_id')
    if message_id:
        dbConnect.deleteMessage(message_id)

    channel = dbConnect.getChannelById(ch_id)
    messages = dbConnect.getMessageAll(ch_id)

    return render_template('detail.html', messages=messages, channel=channel, user_id=user_id)


# リアクション追加
app.route('/reaction_message', methods=['POST'])


def reaction_message():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    ch_id = request.form.get('channel_id')
    if message_id:
        dbConnect.addMeReaction(message_id)

    channel = dbConnect.getChannelById(ch_id)
    messages = dbConnect.getMessageAll(ch_id)

    return render_template('detail.html', messages=messages, channel=channel, user_id=user_id)


# トップ画面へ遷移
@app.route('/')
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')
    else:
        user = dbConnect.getUserById(user_id)
        channels = dbConnect.getChannelAll()
    return render_template('index.html', channels=channels, user=user)

#チャンネル一覧へ遷移
@app.route('/channel')
def chat():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')
    else:
        channels = dbConnect.getChannelAll()
    return render_template('chat.html', channels=channels, user_id=user_id)

#チャット画面へ遷移
@app.route('/detail/<ch_id>')
def detail(ch_id):
    user_id = session.get("user_id")
    if user_id is None:
        return redirect('/login')
    ch_id = ch_id
    channel = dbConnect.getChannelById(ch_id)
    messages = dbConnect.getMessageAll(ch_id)

    return render_template('detail.html', messages=messages, channel=channel, user_id=user_id)

#勉強記録一蘭へ遷移
@app.route('/log')
def log():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')
    else:
        users = dbConnect.getUserById(user_id)
        channels = dbConnect.getChannelAll()
        posts = dbConnect.getPostAll()
        return render_template('log.html', channels=channels, users=users,posts=posts)


#チャンネル作成
@app.route('/add-channel', methods=['POST'])
def add_channel():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')
    ch_name = request.form.get('ch_name')
    channel = dbConnect.getChannelByName(ch_name)
    if channel == None:
        channel_summary = request.form.get('summary')
        main_ca = request.form.get('main_category')
        sub_ca = request.form.get('sub_category')
        dbConnect.addChannel(user_id, ch_name, channel_summary,main_ca,sub_ca)
        return redirect('/chat')
    else:
        error = '既に同じチャンネルが存在します'
        return render_template('error/error.html', error_message=error)


#チャンネル編集
@app.route('/update_channel', methods=['POST'])
def update_channel():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    ch_id = request.form.get('ch_id')
    ch_name = request.form.get('newCh_name')
    channel_summary = request.form.get('newChannel_summary')

    res = dbConnect.updateChannel(user_id, ch_id, channel_summary)
    channel = dbConnect.getChannelById(ch_id)
    messages = dbConnect.getMessageAll(ch_id)
    return render_template('detail.html', message=messages, channel=channel, user_id=user_id)


#チャンネル削除
@app.route('/delete/<ch_id>')
def delete_channel(ch_id):
    user_id = session.get('user_id')
    print(user_id)
    if user_id is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(ch_id)
        print(channel["user_id"] == user_id)
        if channel["user_id"] != user_id:
            flash('チャンネルは作成者のみ削除可能です')
            return redirect('/')
        else:
            dbConnect.deleteChannel(ch_id)
            channels = dbConnect.getChannelAll()
        return render_template('index.html', channels=channels, user_id=user_id)
        hashpassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if hashpassword != user["password"]:
            flash('パスワードが間違っています。')
        else:
            session['user_id'] = user["user_id"]
            return redirect('/')
    return redirect('/login')

#サイドバー（みんなの勉強記録を見る）から勉強記録一覧への遷移
@app.route('/post')
def index_post():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect('/login')
    else:
        posts = dbConnect.getPostAll()
        user = dbConnect.getUser(user_id)

    return render_template('post.html', posts=posts, user=user)

#トップ画面（index.html）から勉強記録一覧への遷移
@app.route('/migration_post')
def mig_post():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect('/login')
    else:
        posts = dbConnect.getPostAll()
        user = dbConnect.getUser(user_id)
    return render_template('post.html', posts=posts, user=user)

#勉強記録追加
@app.route('/add_posts',methods=['POST'])
def add_post():

    post = request.form.get('post')
    study_time = request.form.get('study_time')
    reaction = 0;  #reaction数の初期値

    if post:
        dbConnect.addPost(user_id, post, study_time, reaction)
        return redirect('/')

    posts = dbConnect.getPostAll()
    user = dbConnect.getUser(user_id)

    return render_template('post.html', posts=posts, user=user)

#勉強記録削除
@app.route('/delete_post',methods=['POST'])
def delete_post():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    post_id = request.form.get('post_id')
    if post_id:
        dbConnect.deletePost(post_id)

    posts = dbConnect.getPostAll()
    user = dbConnect.getUser(user_id)

    return render_template('post.html', posts=posts, user=user)

#勉強記録へのいいね追加
@app.route('/reaction_post',methods=['POST'])
def reaction_post():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    post_id = request.form.get('post_id')
    if post_id:
        dbConnect.addPoReaction(post_id)

    posts = dbConnect.getPostAll()
    user = dbConnect.getUser(user_id)

    return render_template('post.html', posts=posts, user=user)

#エラー番号404の際に遷移
@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')

#エラー番号500の際に遷移
@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')

# app.run
if __name__ == '__main__':
    app.run(debug=True)

#目標の設定
@app.route('/set_goal',methods=['POST'])
def set_goal():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    goal = request.form.get('goal')
    return render_template('index.html', goal=goal)

#目標の編集
@app.route('/update_goal',methods=['POST'])
def update_goal():
    goal = session.get('user_id')
    if goal is None:
        return redirect('')

    goal = dbConnect.updateGoal(goal)

#目標日数カウント

def count_goal():
    end_day = datetime(2023, 12, 31)
    today = datetime.now()
    delta = end_day - today
    days = delta.days + 1

    print(days)
