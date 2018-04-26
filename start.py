# -*- coding:utf-8 -*-
import flask_login
from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response, jsonify
import logging
import sys
import os,time
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()


login_manager = LoginManager()

app = Flask(__name__)
db = SQLAlchemy(app)
# URI -> mysql://username:password@server/db
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:CHARLIE4494@localhost:3306/gas'
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "please login and continue"
login_manager.session_protection = "strong"

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger(__name__)
LOG_PATH = 'logs'
LOG_FILE = 'text.txt'

# from model import Gas
class Gas(db.Model):
    __tablename__ = 'gas_repair_info'
    _mobile = db.Column(db.String(100))
    _account = db.Column(db.String(100))
    _date = db.Column(db.String(20))
    _area = db.Column(db.String(20))
    _type = db.Column(db.Integer)
    _address = db.Column(db.String(100))
    _order_id = db.Column(db.String(100),primary_key=True) 

    def __init__(self,_mobile,_account,_date,_area,_type,_address,_order_id):
        self._mobile = _mobile
        self._account = _account
        self._date = _date
        self._area = _area
        self._date = _date
        self._type = _type
        self._address = _address
        self._order_id = _order_id

    def __repr__(self):
        return '<Mobile: %r>' % self._mobile

def config():
    if os.path.exists(LOG_PATH):
        pass
    else:
        os.mkdir(LOG_PATH)
    # 指定logger输出格式
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
    # 文件日志
    file_handler = logging.FileHandler("%s/%s" % (LOG_PATH, LOG_FILE))
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值
    # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # 指定日志的最低输出级别，默认为WARN级别
    logger.setLevel(logging.DEBUG)




@app.route('/', methods=['GET', 'POST'])
@app.route('/index',methods=['GET','POST'])
@flask_login.login_required
def index():
    print("index page is processing ")
    logger.debug("index page")
    logger.debug("cookie name %s" % request.cookies.get('username'))
    print("session::"+session['username'])
    if 'username' in session:
        logger.debug("login user is %s" % flask_login.current_user)
        logger.debug('Logged in as %s' % escape(session['username']))
        return render_template('index.html', name=session['username'])
    else:
        logger.debug("you are not logged in")
        return redirect(url_for('login'))

@app.route('/error')
def error():
    logger.debug("error page")
    return render_template('error.html')

class User(flask_login.UserMixin):
    pass
@login_manager.user_loader
def user_loader(username):
    # if username not in users:
    #     return

    user = User()
    user.id = username
    return user

# 使用request_loader的自定义登录, 同时支持url参数和和使用Authorization头部的基础认证的登录：
@login_manager.request_loader
def request_loader(req):
    logger.debug("request_loader url is %s, request args is %s" % (req.url, req.args))
    authorization = request.headers.get('Authorization')
    logger.debug("Authorization is %s" % authorization)
    # 模拟api登录
    if authorization:
        # get user from authorization
        user = User()
        user.id = 'admin'
        logger.debug("user is %s" % user)
        return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("login processing...")
    # print(request.form)
    if request.method == 'POST':
        # print("login processing...if request.method =='post'")
        logger.debug("login post method")
        username = request.form['username']
        # print('username:'+username)
        password = request.form['password']
        # print("password:"+password)
        next_url = request.args.get("next")
        logger.debug('next is %s' % next_url)
        if username == 'admin' and password == 'admin123':
            user = User()
            user.id = "admin"
            flask_login.login_user(user)
            # flask.flash('Logged in successfully.')
            # user.id = "admin"
            # user.is_authenticated = True
            # flask_login.login_user(user)
            session['username'] = username
            session['password'] = password
            print("session has been set")
            resp = make_response(render_template('index.html'))
            # print("cannot render the index page")
            resp.set_cookie('username', username)
            return resp
            # return jsonify({'status': '0', 'errmsg': '登录成功！'})
        else:
            return render_template('401.html')
            # return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})

    logger.debug("login get method")
    return render_template('login.html')

@app.route('/logout')
@flask_login.login_required          #如果当前没有用户登录，那会返回401，unauthorized
def logout():
    # remove the username from the session if it's there
    logger.debug("logout page")
    session.pop('username', None)
    flask_login.logout_user()  
    return redirect(url_for('login'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/repair_info')
def repair_info():
    return render_template('repair_info.html')
    # pass

@app.route('/account_info')
def account_info():
    return render_template('account_info.html')
    #new

@app.route('/repair_search')
def repair_search():
    return render_template('repair_search.html')
    #new

@app.route('/success',methods=['post'])
def success():
    _mobile = request.form['mobile']
    _account = request.form['account']
    _date = request.form['date']
    _type = int(request.form['type'])
    _area = request.form['area']
    _address = request.form['address_detail']
    _order_id = str(int(time.time()))
    # print(_mobile)
    # print(_account)
    # print(_date)
    # print(_type)
    # print(_area)
    # print(_address)
    # print(_order_id)
    repair_info_data = Gas(_mobile,_account,_date,_area,_type,_address,_order_id)
    db.session.add(repair_info_data)
    db.session.commit()
    return render_template('success.html')

@app.route('/json')
def json():
    return jsonify({'username': session['username'], 'password': session['password']})
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    config()
    app.run(debug=True)
