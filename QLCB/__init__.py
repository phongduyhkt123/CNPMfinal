from flask_login import LoginManager
from flask_admin import Admin
import cloudinary

from QLCB.Database import Database


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

database = Database()
db = database.get_db()
app = database.app

login = LoginManager(app=app)

admin = Admin(app=app, name='FLY', template_mode='bootstrap4')

cloudinary.config(
    cloud_name="djudnibwn",
    api_key="554142242719516",
    api_secret="-qnH-Pc6ibrKyjd9FODdGgI-Q3s"
)
