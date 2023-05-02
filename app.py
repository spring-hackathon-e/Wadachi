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
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')

@app.route('/signup', methods=['POST'])
def usersignup():   # 登録情報の取得
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password1')
    password_chk = request.form.get('password2')

    def isMail(email):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)

    if user_name == '' or email =='' or password == '' or password_chk == '':
        flash('空のフォームがあります')
    elif password != password_chk :
        flash('パスワードが一致していません。')
    elif isMail(email) is None:
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
        return redirect('/')
    return redirect('/signup')   # 入力情報のクリア

#ログイン
@app.route('/login')
def login():
    return render_template('registration/login.html')

@app.route('/login', methods=['POST'])
def userlogin(): #user_idとemailを格納先と照合
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = dbConnect.getUserId(email)

    if user == None:
        flash('ユーザーIDが間違っています。')
    else:
        hashpassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if hashpassword != user[password] :
            flash('パスワードが間違っています。')
        else:
            session['user_id'] = user["user_id"]
            return redirect('/')
    return redirect('/login')

#ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
