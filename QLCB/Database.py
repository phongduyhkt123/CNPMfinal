from flask_sqlalchemy import SQLAlchemy


class Database:
    __db = None
    app = None

    def __init__(self, app):
        self.app = app

    def get_db(self):
        if self.__db is None:
            self.__db = SQLAlchemy(self.app)
        return self.__db
