from flask import Flask, request, redirect, render_template, session, flash
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib
import uuid
import re

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)

#サインイン
@app.route('/signin')
def signup():
    return render_template('registration/signin.html')

@app.route('/signin', methods=['POST'])
def signup(): #登録情報の取得
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    user_id = request.form.get('name')
    password = request.form.get('password')
    password_chk = request.form.get('password_chk')

    def isMail(email):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)


    if user_id == '' or email =='' or password == '' or password_chk == '':
        flash('空のフォームがあります')
    elif password != password_chk :
        flash('パスワードが一致していません。')
    elif isMail(email) is None:
        flash('正しいメールアドレスを記入してください。')
    else:
        user_id = uuid.uuid4
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = User(user_id, user_name, email, password)
        DBuser = dbConnect.getUser(email)

    if DBuser != None: #emailが登録済み
        flash('すでに登録済みのユーザーです。')
    else:
        dbConnect.createUser(user)
        UserId = str(user_id)
        session['user_id'] = UserId
        return redirect('/')
    return redirect('/signup')  #間違ってる所をクリア、色塗りの方がいいんじゃ

# チャンネル一覧
@app.route('/')
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')
    else:
        channels = dbConnect.getChannelAll()
        return render_template('index.html', channels=channels, user_id=user_id)

# チャンネル作成
@app.route('/add_channel', methods=['POST'])
def add_channel():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')
    ch_name = request.form.get('ch_name')
    channel = dbConnect.getChannelByName(ch_name)
    if channel == None:
        channel_summary = request.form.get('channel-summary')
        dbConnect.addChannel(user_id,ch_name,channel_summary)
        return redirect('/')
    else:
        error = '既に同じチャンネルが存在します'
        return render_template('error/error.html', error_message=error)

# チャンネル編集
@app.route('/update_channel',methods=['POST'])
def update_channel():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    ch_id = request.form.get('ch_id')
    ch_name = request.form.get('ch_name')
    channel_summary = request.form.get('channel_summary')

    res = dbConnect.updateChannel(user_id, ch_id, channel_summary)
    channel = dbConnect.getChannelById(ch_id)
    messages = dbConnect.getMessageAll(ch_id)
    return render_template('detail.html', message=messsage, channel=channel, user_id=user_id)

# チャンネル削除
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
            return redirect ('/')
        else:
            dbConnect.deleteChannel(ch_id)
            channels = dbConnect.getChannelAll()
        return render_template('index.html', channels=channels, user_id=user_id)


