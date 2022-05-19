from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Database:
    __db = None
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/qlcbdb?charset=utf8mb4"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'super secret key'

    def get_db(self):
        if self.__db is None:
            self.__db = SQLAlchemy(self.app)
        return self.__db



