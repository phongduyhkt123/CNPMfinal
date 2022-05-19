from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
import cloudinary

from QLCB.Database import Database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/qlcbdb?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config["PAGE_SIZE"] = 2

KEY_ADMIN_ROLE = "Admin"
KEY_EMPLOYEE_ROLE = "Employee"

KEY_TICKET_TYPE_BUSINESS = "Business Class"
KEY_TICKET_TYPE_ECONOMY = "Economy Class"

DATA = [
    {
        # "airports":
        #     [
        #         {"airportName": "Tân Sơn Nhất", "airportAddress": "TP HCM"},
        #         {"airportName": "Nội Bài", "airportAddress": "Hà Nội"},
        #         {"airportName": "Quy Nhơn", "airportAddress": "Quy Nhơn"},
        #         {"airportName": "Huế", "airportAddress": "Huế"}
        #     ],

        "roles":
            [
                {"roleName": KEY_ADMIN_ROLE},
                {"roleName": KEY_EMPLOYEE_ROLE},
            ],

        "ticket_types":
            [
                {"typeName": KEY_TICKET_TYPE_BUSINESS},
                {"typeName": KEY_TICKET_TYPE_ECONOMY},
            ]
    }
]

app.secret_key = 'super secret key'


database = Database(app)
db = database.get_db()

login = LoginManager(app=app)

admin = Admin(app=app, name='FLY', template_mode='bootstrap4')

cloudinary.config(
    cloud_name="djudnibwn",
    api_key="554142242719516",
    api_secret="-qnH-Pc6ibrKyjd9FODdGgI-Q3s"
)
