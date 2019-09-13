import os
from jogoteca import app

SECRET_KEY = 'alura'
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "1Coxinh@"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'