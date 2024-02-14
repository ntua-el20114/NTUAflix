from flask import Flask
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)

app.config["SECRET_KEY"] = "SECRET_KEY"
app.config["MYSQL_DB"] = "ntuaflix"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_HOST"] = "127.0.0.1"
#app.config["MYSQL_CHARSET"] = "utf8"
# # app.config["MYSQL_PORT"] = 5000
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#db = MySQL(app)
db = MySQL(app,
           prefix="ntuaflix",
           host="localhost",
           user="root",
           password="",
           db="ntuaflix",
           #autocommit=True,
           cursorclass=pymysql.cursors.DictCursor
           )

db.init_app(app)
