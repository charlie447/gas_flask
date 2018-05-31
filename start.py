# -*- coding:utf-8 -*-
import flask_login
from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response, jsonify,Response
import logging
import sys
import os,time
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

# reload(sys)
# sys.setdefaultencoding('utf-8')

login_manager = LoginManager()

app = Flask(__name__)
# db = SQLAlchemy(app)
# URI -> mysql://username:password@server/db
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:CHARLIE4494@localhost:3306/gas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
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

class Users(db.Model):
    __tablename__ = 'gas_user'
    username = db.Column(db.String(20),primary_key=True)
    password = db.Column(db.String(20))
    mobile = db.Column(db.String(100),primary_key=True)
    
    def __init__(self,username,password,mobile):
        self.username = username
        self.password = password
        self.mobile = mobile

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
        gas_user = Users.query.filter_by(username=username).first()  # 从数据库中获得一个gas_user对象，同select语句
        # print("password:"+password)
        next_url = request.args.get("next")
        logger.debug('next is %s' % next_url)
        if gas_user is not None and password == gas_user.password:
            user = User()
            user.id = gas_user.username
            flask_login.login_user(user)
            # flask.flash('Logged in successfully.')
            # user.id = "admin"
            # user.is_authenticated = True
            # flask_login.login_user(user)
            session['username'] = username
            session['password'] = password
            session['mobile'] = gas_user.mobile
            print("session has been set")
            resp = make_response(render_template('index.html',name=session['username']))
            # print("cannot render the index page")
            resp.set_cookie('username', username)
            
            return resp
            # return jsonify({'status': '0', 'errmsg': '登录成功！'})
        else:
            return render_template('401.html')
            # return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})

    logger.debug("login get method")
    return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    print("signup processing")
    if request.method == 'POST':
        # print("login processing...if request.method =='post'")
        logger.debug("signup post method")
        username = request.form['username']
        # print('username:'+username)

        password = request.form['password']
        re_password = request.form['re-password']
        mobile = request.form['mobile']
        # print("password:"+password)
        gas_user = Users.query.filter_by(username=username).first()  # 从数据库中获得一个gas_user对象，同select语句
        gas_user_by_mobile = Users.query.filter_by(mobile=mobile).first()
        next_url = request.args.get("next")
        logger.debug('next is %s' % next_url)
        if gas_user is None and gas_user_by_mobile is None:
            # 如果两次密码不同，定向到401
            if password != re_password:
                return render_template('401.html')
            
            new_user = Users(username,password,mobile)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')

        else:
            return render_template('401.html')
            # return jsonify({'status': '-1', 'errmsg': '用户名或密码错误！'})
        # 注册不通过有几种情况，用户名已存在，手机号已被注册，两次密码不同，但都暂时定向到401，
    logger.debug("signup get method")
    return render_template('signup.html')

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
    context = {
        "username":session['username'],
        "mobile":session['mobile']
    }
    return render_template('repair_info.html',**context)
    # pass

@app.route('/user')
def account_info():
    context = {
        "username":session['username'],
        "mobile":session['mobile']
    }
    print(session["password"])
    return render_template('user.html',**context)
    #new

@app.route('/repair_search')
def repair_search():
    table_data_list = []
    if session['username']=='admin':
        data = Gas.query.all()   # 获得所有repair_info的数据，admin返回的是所有对象列表
    else:
        data = Gas.query.filter_by(_account=session['username']).all()  # 普通用户
    
    if len(data) !=0:
        
        for data_obj in data:
            tmp = {
                "account":data_obj._account,
                "mobile":data_obj._mobile,
                "area":data_obj._area,
                "address":data_obj._address,
                "type":data_obj._type,
                "order_id":data_obj._order_id
            }
            table_data_list.append(tmp) 
        context = {
            "username":session['username'],
            "mobile":session['mobile'],
            "table_data":table_data_list
        }
    else:
        context = {
            "username":session['username'],
            "mobile":session['mobile'],
            "table_data":[{
                "account":"无记录",
                "mobile":"无记录",
                "area":"无记录",
                "address":"无记录",
                "type":"无记录",
                "order_id":"无记录"
            }]
        }
    # print(context)
    return render_template('repair_search.html',**context)
    #new
@app.route('/repair_search/get_result_by_id',methods=['POST'])
def get_result_by_id():
    table_data_list = []
    order_id = request.form['order_id']
    data = Gas.query.filter_by(_order_id = order_id).all()
    if len(data) !=0:
        
        for data_obj in data:
            tmp = {
                "account":data_obj._account,
                "mobile":data_obj._mobile,
                "area":data_obj._area,
                "address":data_obj._address,
                "type":data_obj._type,
                "order_id":data_obj._order_id
            }
            table_data_list.append(tmp) 
        context = {
            "username":session['username'],
            "mobile":session['mobile'],
            "table_data":table_data_list
        }
    else:
        context = {
            "username":session['username'],
            "mobile":session['mobile'],
            "table_data":[{
                "account":"无记录",
                "mobile":"无记录",
                "area":"无记录",
                "address":"无记录",
                "type":"无记录",
                "order_id":"无记录"
            }]
        }
    # print(context)
    return render_template('repair_search.html',**context)
@app.route('/success',methods=['POST'])
def success():
    _mobile = request.form['mobile']
    _account = session['username']
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

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/baidu_maps')
def loading_map():
    return render_template('baidu_maps.html')

@app.route('/ajax_test')
def test_ajax():
    return render_template('ajax_test.html')
@app.route('/ajax/<name>',methods=['POST','GET'])
def query_info_by_name(name):
    table_data_list = []
    data = Gas.query.filter_by(_account=name).all()
    for data_obj in data:
        tmp = {
            "account":data_obj._account,
            "mobile":data_obj._mobile,
            "area":data_obj._area,
            "address":data_obj._address,
            "type":data_obj._type,
            "order_id":data_obj._order_id
        }
        table_data_list.append(tmp)   
    return jsonify(table_data_list)

@app.route('/api/getChartData/<index>',methods=['GET','POST'])
def get_chart_data(index):
    data_list = [
        [5, 20, 36, 10, 10, 20],
        [2, 8, 29, 21, 20, 30],
        [1, 30, 36, 20, 30, 10],
        [5, 26, 30, 16, 12, 17]
    ]
    i = int(index)
    return jsonify(data_list[i])

@app.route('/json')
def json():
    return jsonify({'username': session['username'], 'password': session['password']})

@app.route('/ajax/verify_password')
def verify_password():
    pwd = request.args['pwd']
    data = {
        "status":"ok"
    }
    if pwd == session['password']:
        return jsonify(data)
    else:
        data["status"] = "no"
        return jsonify(data)

@app.route('/ajax/change_password',methods=['POST'])
def change_password():
    print(".........ready")
    new_password = request.form['password']
    print(new_password)
    data = {
        "status":"ok"
    }
    q = Users.query.filter_by(username = session['username']).update(dict(password = new_password))
    db.session.commit()
    return jsonify(data)

@app.route('/ajax/update_mobile', methods=['POST'])
def update_mobile():
    new_mobile = request.form['mobile']
    data = {
        "status":"ok"
    }
    q = Users.query.filter_by(username = session['username']).update(dict(mobile = new_mobile))
    db.session.commit()
    session['mobile'] = new_mobile
    return jsonify(data)    

'''
以下路由只是用来测试ajax功能的
'''
@app.route('/mystring')
def mystring():
    return 'my string'

@app.route('/dataFromAjax')
def dataFromAjax():
    test = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'

@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)

@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    return jsonify(l)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    config()
    app.run(debug=True)
