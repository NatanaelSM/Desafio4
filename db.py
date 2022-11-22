from app import app
from flask_mysql import Mysql

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'desafioilm'

mysql = Mysql(app)