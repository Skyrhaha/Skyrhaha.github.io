## Flask安装

> 介绍
- 官方文档https://dormousehole.readthedocs.io/en/latest/index.html
- Flask为python语言的轻量级web框架
- Flask vs Django
  - Django大而全
  - Flask更偏向提供轻量级api服务
- Flask通过Flask-sqlalchemy访问数据库 http://www.pythondoc.com/flask-sqlalchemy/quickstart.html

> 安装
```bash
# 切换python虚拟环境为pyspark
conda activate pyspark

# 安装Flask
pip install Flask

# 检查Flask版本
import flask
flask.__version__
'2.1.2'
```

## Flask应用app.py编写
```python
# myflasker/app.py
# coding:utf8

'''
本演示代码参考官方文档quickstart:
https://dormousehole.readthedocs.io/en/latest/quickstart.html
'''
from flask import make_response, redirect, session, url_for
from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
from flask import abort
import os

app = Flask(__name__)

# 秘钥设置
app.secret_key=os.urandom(16)

@app.route("/")
def index():
    # 已登录的返回登陆信息
    if 'username' in session:
        # return f'Logged in as {session["username"]}'
        return f'''
        <p>Logged in as {session["username"]}</p>
        <form action="logout">
            <input type="submit" value="Logout" />
        </form>
        '''
    
    # 未登录的重定向到登录页
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 模拟登陆成功设置session
        # 然后重定向到index
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        # 返回登陆页
        return '''
        <form method='post'>
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
        '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# 接口路径参数、查询参数、cookies使用演示
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    print('request=', request)
    searchWord = request.args.get('key', '')
    print('searchWord=', searchWord)
    token = request.cookies.get('token', '')
    print(f'token={token}')

    # return render_template('hello.html', name=name)

    rt = render_template('hello.html', name=name)
    resp = make_response(rt)
    resp.set_cookie('token', 'the_token')
    return resp

# 文件上传演示
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    file = request.files['file']
    # 获取上传文件的源文件名
    file.save(f'/home/dev/test/upload/{secure_filename(file.filename)}')
    return "success"

# 404页面演示
@app.route("/404", methods=['GET', 'POST'])
def error():
    abort(404)

# 404页面设置
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

# Restful API演示: 返回JSON
@app.route("/me")
def me_api():
    return {
        "username": "M",
        "theme": "theme",
        "image": url_for("static", filename="style.css"),
    }

if __name__ == '__main__':
    print('app.run()...')
    app.run(port=5000)
```

## 开发环境运行
### 使用flask运行
```bash
# 切换到app.py目录
cd myflasker/ 

#设置环境变量FLASK_APP
export FLASK_APP=app #不设置默认为app

#运行
flask run

运行结果:
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

注意: 此种方式不会执行__name__ == '__main__'的内容
```

### 使用python运行
```bash
# 通过python -m app 或 python app.py 

# 切换到app.py目录
cd myflasker/

#python -m app
python app.py

运行结果:
app.run()...
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8080 (Press CTRL+C to quit)

通过运行输出日志可见LISTEN PORT为8080

注意: 此种方式会执行__name__ == '__main__'的内容
 ```

## 生产环境部署Flask应用
### uWSGI服务器安装
```bash
uwsgi官方文档:
https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html

# 切换到使用的python虚拟环境(我这里是pyspark)
conda activate pyspark

# 通过pip安装uwsgi
pip install uwsgi
# 报错找不到libpython3.9.a
# => 是因为python觉得python.xx.a文件大家日常使用较少，所以在新版本中默认不生成python.xx.a文件

# 因此需要编译python源代码来生成libpython3.9.a文件
# 下载python3.9.12版本源代码(我本地anaconda3 python版本为3.9.12)
wget https://www.python.org/ftp/python/3.9.12/Python-3.9.12.tgz

#解压
tar xzvf Python-3.9.12.tgz  

#进入源码目录
cd Python-3.9.12 

#编译器配置安装目录
./configure --prefix=/tmp/python3.9.12 

#注意不要带上--enable-optimizations参数，会导致gcc版本问题
#./configure --prefix=/tmp/python3.9.12 --enable-optimizations

#编译
make 

#安装,会安装在之前设置的/tmp/python3.9.12目录
make install 

#进入安装目录
cd /tmp/python3.9.12 

# 复制libpython3.9.a到指定的目录（pip install uwsgi报错会提示在config-3.9-x86_64-linux-gnu目录找不到libpython3.9.a文件）
cp libpython3.9.a /export/server/anaconda3/envs/pyspark/lib/python3.9/config-3.9-x86_64-linux-gnu/

# 重新执行uwsgi安装
pip install uwsgi
#继续报错: collect2: error: ld returned 1 exit status
#类似问题是gcc或依赖库版本不兼容导致
#查询资料后给出解决办法是使用conda来安装uwsgi
conda install uwsgi
#使用conda安装还是失败，查询资料后还是依赖的库或版本不兼容导致
#给出解决办法是设置conda的channel（类似maven仓库源)
#然后更新conda
#然后重新安装
#conda channel具体可参考https://www.jianshu.com/p/eba58694537b

#设置channel为conda-forge
conda config --add channels conda-forge

#查看当前channels
conda config --get channels

# 安装conda
conda install conda

# 更新conda
conda update conda

# 重新安装uwsgi
conda install uwsgi
安装成功

#查看uwsgi版本
uwsgi --version
2.0.20

#查看uwsgi对应python版本
uwsgi --python-version
3.9.12
```

### 创建uwsgi应用配置文件
```ini
config.ini
#在项目根目录(myflasker/)创建配置文件config.ini

[uwsgi]
master=true

#python代码热更新
py-autoreload=1

#uwsgi启动时，所使用的地址和端口（这个是http协议的）
http=0.0.0.0:8000

#指向网站目录
chdir=/home/dev/test/pyspark/myflasker/

#python 启动程序文件
wsgi-file=app.py

#python 程序内用以启动的application 变量名
callable=app

#处理器数
processes=4

#线程数
threads=2

uid=dev
gid=dev

# uwsgi的进程名称前缀
procname-prefix-spaced=etd 

# 退出uwsgi是否清理中间文件，包含pid、sock和status文件
vacuum=true 

# socket文件，配置nginx时候使用
# socket=%(chdir)/uwsgi/uwsgi.sock
# status文件，可以查看uwsgi的运行状态
#stats=%(chdir)/uwsgi/uwsgi.status 
# pid文件，通过该文件可以控制uwsgi的重启和停止
pidfile=%(chdir)/uwsgi/uwsgi.pid 
# 日志文件，通过该文件查看uwsgi的日志
daemonize=%(chdir)/uwsgi/uwsgi.log 
```

### 运行
```bash
#进入项目根目录
cd myflasker/

#创建uwsgi目录
mkdir uwsgi

#启动
uwsgi config.ini 
[uWSGI] getting INI configuration from config.ini

#查看进程
ps -ef|grep etd
dev       9388 27859  0 21:05 ?        00:00:02 etd uWSGI worker 1
dev       9389 27859  0 21:05 ?        00:00:02 etd uWSGI worker 2
dev       9392 27859  0 21:05 ?        00:00:02 etd uWSGI worker 3
dev       9393 27859  0 21:05 ?        00:00:02 etd uWSGI worker 4
dev       9394 27859  0 21:05 ?        00:00:00 etd uWSGI http 1
root     20149 11597  0 21:47 pts/5    00:00:00 grep --color=auto etd
dev      27859     1  0 20:14 ?        00:00:11 etd uWSGI master

uwsgi --ini uwsgi.ini # 启动
uwsgi --reload uwsgi.pid # 重启
uwsgi --stop uwsgi.pid # 关闭
```

## 访问
浏览器访问`http://ip:8000/`返回登录页面


## 根据表自动生成Model代码
```bash
pip install sqlacodegen
sqlacodegen `echo $SQLALCHEMY_DATABASE_URI` --outfile=models.py --tables t_sys_user,t_sys_user_role,t_sys_role,t_sys_role_resource,t_sys_resource,t_sys_resource_api,t_sys_api,t_sys_dict,t_sys_param,t_sys_login
```

## sqlachemy操作数据库
## sqlachemy查询结果json序列化
## 全局异常捕获