## 快速开始
1. 安装Python 3.6环境，此处略过。
   可选步骤：
   - 安装virtualenv 虚拟环境，这个步是为了让你的项目开发环境独立出来，以免影响Python在系统中的环境。用pip安装即可，`pip3 install virtualenv` ，在终端黎输入 `virtualenv --version` 检查是否安装程控。
   - 新建`Python 3` 虚拟环境。在项目环境下执行 `virtualenv project_env_name -p python3`， 即可新建`python 3`虚拟环境。（`-p python3` 是指定虚拟环境所用的Python版本）
   - 激活虚拟环境。` source ./project_env_name/bin/activate` ，激活了虚拟环境之后，就可以在这个环境安装所需要的依赖包而不影响外部环境。
2. 用git把项目克隆到本地，`git clone https://github.com/charlie447/flask_demo.git`
3. 安装依赖。所需依赖详情见`requirements.txt`。可利用`pip`安装，如果依赖很多，可通过`pip install -r requirements.txt` 直接安装。
4. 启动本项目。确保在你安装的环境中运行。`python start.py`
***
## 关于mysql *
1. 安装依赖`pymysql`
2. 建立数据库：
    - 需要创建一个`gas` 数据库
    - 在`start.py` 里修改如下代码：
        ```
        # URI -> mysql://username:password@server/db
        app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:CHARLIE4494@localhost:3306/gas'
        ```
    - 进入Python shell `python`
        ```
        from start import db
        db.create_all()
        ```
    即可创建数据库模型
    - 在 `test.py` 里面有测试用例，执行就可以插入一条数据到`gas_repair_info` 表里边。
## 重要提示
- 图表数据在demo.js中修改
- 关于数据库的创建和SQLAlchemy 参考：http://www.pythondoc.com/flask-sqlalchemy/quickstart.html
- python3 不支持MySQL-python,可以用pymysql代替，解决方法如：https://blog.csdn.net/jabony/article/details/77483273
    在项目下的__init__.py中添加：
    ```
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

## git 相关
1. 如何把master分支merge 到 其他分支？
    `git branch` 检查分支
    `git checkout irene` 切换到其他分支
    `git merge master` 开始merge
    不过这好像很不符合正常的项目开发的版本管理
2. 