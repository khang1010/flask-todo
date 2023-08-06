import os

basedir = os.path.abspath(os.path.dirname(__file__))
# Cấu hình đường dẫn đến cơ sở dữ liệu SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todo.db')